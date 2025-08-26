import os
from pathlib import Path
from datetime import timedelta
import environ
from .social_config import SOCIAL_AUTH_CONFIGS

# Load environment variables from .env file
env = environ.Env()
<<<<<<< HEAD
environ.Env.read_env(Path(__file__).resolve().parent.parent / '.env')
=======
environ.Env.read_env(Path(__file__).resolve().parent.parent / '.env.example')
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d

# Base directory of the projectfrom pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^c&x94b&90z82ckyu04-8dki$@9)2q33-oh4n4qp6%e687wr*-'


# Debug mode flag (False in base settings, overridden in development)
DEBUG = False

# Hosts/domain names that are valid for this site
<<<<<<< HEAD
ALLOWED_HOSTS = ['*']
=======
ALLOWED_HOSTS = ['syncflow-backend-production.up.railway.app']
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d

# Installed Django applications
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.apple',
    'dj_rest_auth.registration',
    'drf_spectacular',
    'django_celery_beat',
    'csp',

    # Custom apps
<<<<<<< HEAD
    'AIs',
    'analytics',
    'automations',
    'campaigns',
    'contents',
    'core',
    'integrations',
    'social',
    'UserAccount',
=======
    'apps.AIs',
    'apps.analytics',
    'apps.automations',
    'apps.campaigns',
    'apps.contents',
    'apps.core',
    'apps.integrations',
    'apps.social',
    'apps.UserAccount',
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
]

# Middleware configuration
MIDDLEWARE = [
<<<<<<< HEAD
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
=======
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
]

# Root URL configuration module
ROOT_URLCONF = 'syncfloww.urls'

# Template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR / 'templates'],  #' Template directories
=======
        'DIRS': [BASE_DIR / 'templates'],  # Template directories
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
        'APP_DIRS': True,  # Enable app template loading
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application callable
WSGI_APPLICATION = 'syncfloww.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD
=======
# Custom user model
AUTH_USER_MODEL = 'UserAccount.User'

>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Site ID for django.contrib.sites
SITE_ID = 1

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# dj-allauth / dj-rest-auth email login settings
<<<<<<< HEAD
# # ACCOUNT_USER_MODEL_USERNAME_FIELD = None
AUTH_USER_MODEL = "UserAccount.CustomUser"

ACCOUNT_SESSION_REMEMBER = True

LOGIN_URL = '/accounts/login/'
SIGNUP_URL = '/accounts/signup/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGIN_REDIRECT_URL = '/'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# Signup fields configuration
# ACCOUNT_SIGNUP_FIELDS = {
#     "email": {"required": True},
#     "first_name": {"required": True},
#     "last_name": {"required": True},
#     "password1": {"required": True},
#     "password2": {"required": True},
# }
ACCOUNT_SIGNUP_FIELDS = ['email*', 'first_name*', 'last_name*', 'password1*', 'password2*']
ACCOUNT_LOGIN_METHODS = {'email'}
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# AUTHENTICATION_METHOD = "email"
=======
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

<<<<<<< HEAD
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# Login only with email
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = env('EMAIL_BACKEND')
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env.int('EMAIL_PORT')
# EMAIL_USE_TLS = env('EMAIL_USE_TLS')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
=======
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d


# REST auth configuration
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'syncfloww-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'syncfloww-refresh-token',
    'JWT_AUTH_HTTPONLY': False,
    'SESSION_LOGIN': False,
<<<<<<< HEAD
    'REGISTER_SERIALIZER': 'UserAccount.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'UserAccount.serializers.UserSerializer',
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password-reset-confirm/{uid}/{token}',
    'PASSWORD_CHANGE_SERIALIZER': 'UserAccount.serializers.CustomPasswordChangeSerializer',
=======
    'REGISTER_SERIALIZER': 'apps.UserAccount.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'apps.UserAccount.serializers.UserSerializer',
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password-reset-confirm/{uid}/{token}',
    'PASSWORD_CHANGE_SERIALIZER': 'apps.UserAccount.serializers.CustomPasswordChangeSerializer',
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
}

# Simple JWT settings for token lifetimes and rotation
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# Social account providers configuration for OAuth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': [
            'id',
<<<<<<< HEAD
            'email',''
=======
            'email',
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ]
    }
}

# Social account providers with app credentials loaded from environment variables
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': env('GOOGLE_OAUTH2_CLIENT_ID'),
            'secret': env('GOOGLE_OAUTH2_CLIENT_SECRET'),
            'key': ''
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'APP': {
            'client_id': env('FACEBOOK_APP_ID'), 
            'secret': env('FACEBOOK_APP_SECRET'),
            'key': ''
        }
    }
}

# Django REST Framework settings for authentication, pagination, filtering, and permissions
REST_FRAMEWORK = {
<<<<<<< HEAD
    'DEFAULT_AUTHENTICATION_CLASSES': ("rest_framework_simplejwt.authentication.JWTAuthentication",),
=======
    'DEFAULT_AUTHENTICATION_CLASSES': ('dj_rest_auth.jwt_auth.JWTCookieAuthentication',),
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.AllowAny',
    ],
}

# DRF Spectacular API schema settings
SPECTACULAR_SETTINGS = {
    'TITLE': env('SPECTACULAR_SETTINGS_TITLE'),
    'DESCRIPTION': env('SPECTACULAR_SETTINGS_DESCRIPTION'),
    'VERSION': env('SPECTACULAR_SETTINGS_VERSION'),
    'SERVE_INCLUDE_SCHEMA': False,
}

# CORS allowed origins for cross-origin requests
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "https://syncflow-frontend-production.up.railway.app",
<<<<<<< HEAD
    "https://preview--prompt-reach-ai.lovable.app",
    "http://localhost:3000",   # keep if you also dev locally
    "http://localhost:5173",
=======
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
]

# CORS allowed origins (alternative, commented out)
# CORS_ALLOWED_ORIGINS = [
#     env('FRONTEND_URL'),
# ]

# Allow credentials in CORS requests
CORS_ALLOW_CREDENTIALS = True
<<<<<<< HEAD
# Trusted origins for CSRF protection
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "https://syncflow-frontend-production.up.railway.app",
    "https://preview--prompt-reach-ai.lovable.app",
    "http://localhost:3000",   # keep if you also dev locally
    "http://localhost:5173",
]
=======

# Trusted origins for CSRF protection
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "http://localhost:8000", "syncflow-backend-production.up.railway.app", "https://syncflow-frontend-production.up.railway.app"]
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d

# Cookie settings for session and CSRF
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Celery configuration for asynchronous task queue
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Content Security Policy settings
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ("'self'",),
        "script-src": ("'self'", "https://cdn.jsdelivr.net", "'unsafe-inline'"),
        "style-src": ("'self'", "https://fonts.googleapis.com", "'unsafe-inline'"),
        "font-src": ("'self'", "https://fonts.gstatic.com"),
    }
}

# Custom account adapter for user account management
<<<<<<< HEAD
ACCOUNT_ADAPTER = 'UserAccount.adapters.CustomAccountAdapter'
=======
ACCOUNT_ADAPTER = 'apps.UserAccount.adapters.CustomAccountAdapter'
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d

# DRF Spectacular API documentation settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'SyncflowwAI API',
    'DESCRIPTION': 'API for SyncflowwAI social media marketing platform',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# Social authentication configurations imported from social_config module
SOCIAL_AUTH_CONFIGS = SOCIAL_AUTH_CONFIGS

# Hugging Face API key and model configuration
<<<<<<< HEAD
HUGGINGFACE_API_KEY = env('HUGGINGFACE_API_KEY')
=======
HUGGINGFACE_API_KEY = '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'
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
HUGGINGFACE_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Default large language model providers configuration
DEFAULT_LLM_PROVIDERS = [
    {
        'name': 'HuggingFace',
<<<<<<< HEAD
        'provider_class': 'automations.providers.huggingface.HuggingFaceProvider',
=======
        'provider_class': 'apps.automations.providers.huggingface.HuggingFaceProvider',
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
        'api_key_env': 'HUGGINGFACE_API_KEY',
        'base_url': 'https://api-inference.huggingface.co'
    },
    {
        'name': 'OpenAI',
<<<<<<< HEAD
        'provider_class': 'automations.providers.openai.OpenAIProvider',
=======
        'provider_class': 'apps.automations.providers.openai.OpenAIProvider',
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d
        'api_key_env': 'OPENAI_API_KEY',
        'base_url': 'https://api.openai.com/v1'
    }
]


# Logging configuration (commented out)
# # LOGGING = {
# #     'version': 1,
# #     'disable_existing_loggers': False,
# #     'handlers': {
# #         'console': {
# #             'class': 'logging.StreamHandler',
# #         },
# #     },
# #     'loggers': {
# #         'django.request': {
# #             'handlers': ['console'],
# #             'level': 'WARNING',  # Change to WARNING or ERROR
# #             'propagate': False,
# #         },
# #     },
# # }


