from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
import logging

from . import models

logger = logging.getLogger(__name__)


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            logger.debug("No JWT token found in cookies")
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            logger.debug(f"JWT token decoded successfully for user ID: {payload.get('id')}")
        except jwt.ExpiredSignatureError:
            logger.warning("JWT token has expired")
            raise exceptions.AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError as e:
            logger.warning(f"Invalid JWT token: {str(e)}")
            raise exceptions.AuthenticationFailed("Invalid token")
        except Exception as e:
            logger.error(f"JWT decode error: {str(e)}")
            raise exceptions.AuthenticationFailed("Token decode failed")

        user = models.User.objects.filter(id=payload["id"]).first()

        if not user:
            logger.warning(f"User not found for ID: {payload['id']}")
            raise exceptions.AuthenticationFailed("User not found")

        if not user.is_active:
            logger.warning(f"Inactive user attempted access: {user.email}")
            raise exceptions.AuthenticationFailed("User account is disabled")

        logger.debug(f"Authentication successful for user: {user.email}")
        return (user, None)
