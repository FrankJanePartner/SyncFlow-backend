from rest_framework import views, response, exceptions, permissions, status
from . import serializer as user_serializer
from . import services, authentication
from .services import UserDataClass


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


class LoginApi(views.APIView):
    """
    Login with email + password.
    Returns JWT in cookie and response body.
    """

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise exceptions.AuthenticationFailed("Email and password are required.")

        user = services.user_email_selector(email=email)

        if user is None or not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid credentials.")

        if user.id is not None:
            token = services.create_token(user_id=user.id)
        else:
            raise exceptions.AuthenticationFailed("User ID is not available.")

        resp = response.Response(
            {
                "detail": "Login successful.",
                "token": token,
                "user": user_serializer.UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )
        resp.set_cookie(key="jwt", value=token, httponly=True)

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
