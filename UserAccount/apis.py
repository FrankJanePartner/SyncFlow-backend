from rest_framework import views, response, exceptions, permissions, status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import serializer as user_serializer
from . import services, authentication
from .services import UserDataClass


@method_decorator(csrf_exempt, name="dispatch")
class RegisterApi(views.APIView):
    """
    User registration endpoint.
    Creates a new user, returns the user data + JWT token.
    """

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        user_dc = UserDataClass(**data)

        # Create user
        serializer.instance = services.create_user(user_dc=user_dc)

        # Auto-issue JWT
        if serializer.instance.id is not None:
            token = services.create_token(user_id=serializer.instance.id)
        else:
            raise exceptions.ValidationError("User ID is not available.")

        return response.Response(
            {
                "user": serializer.data,
                "detail": "Registration successful.",
                "token": token,
            },
            status=status.HTTP_201_CREATED,
        )


@method_decorator(csrf_exempt, name="dispatch")
class LoginApi(views.APIView):
    authentication_classes = []  # disable session/CSRF for API
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return response.Response(
                {"detail": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = services.user_email_selector(email)
        if user is None or not user.check_password(password):
            return response.Response(
                {"detail": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token = services.create_token(user.id)
        resp = response.Response(
            {
                "token": token,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            },
            status=status.HTTP_200_OK,
        )
        # Set JWT token as cookie for compatibility
        resp.set_cookie(
            key="jwt",
            value=token,
            httponly=True,
            secure=True,
            samesite="Lax",
        )
        return resp


class UserApi(views.APIView):
    """
    Returns the currently authenticated user's data.
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = user_serializer.UserSerializer(request.user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name="dispatch")
class LogoutApi(views.APIView):
    """
    Logs out the current user by clearing JWT cookie.
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response(
            {"detail": "Logout successful."},
            status=status.HTTP_200_OK,
        )
        resp.delete_cookie("jwt")
        return resp
