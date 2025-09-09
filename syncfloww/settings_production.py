"""
Production settings for SyncFloww backend.
This file contains production-specific settings.
"""

from .settings import *

# Override settings for production
DEBUG = False

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Allowed hosts for production
ALLOWED_HOSTS = [
    "syncfloww.onrender.com",
    "https://syncfloww.onrender.com",
    "https://preview--prompt-reach-ai.lovable.app",  # Add frontend origin
]

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://syncfloww.onrender.com",
    "https://preview--prompt-reach-ai.lovable.app",
]

CORS_ALLOW_CREDENTIALS = True

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://syncfloww.onrender.com",
    "https://preview--prompt-reach-ai.lovable.app",
]

# Logging for production
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
