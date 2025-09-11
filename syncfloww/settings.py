import os
from pathlib import Path
from datetime import timedelta
import environ
# from supabase import create_client, Client
from .social_config import SOCIAL_AUTH_CONFIGS
import dj_database_url


env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")
JWT_SECRET = os.environ.get("JWT_SECRET", "dev-secret-key")


# Debug mode flag (False in base settings, overridden in development)
DEBUG = True

# Hosts/domain names that are valid for this site
ALLOWED_HOSTS = ["https://syncfloww-backend.onrender.com", "https://syncfloww.onrender.com", "http://localhost:8000", "http://127.0.0.1:8000", "localhost:8000", 'syncfloww-backend.onrender.com', 'syncfloww.onrender.com', "https://preview--prompt-reach-ai.lovable.app", "preview--prompt-reach-ai.lovable.app"]

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
    'social_django',
    'django_celery_beat',
    'csp',

    # Custom apps
    'AIs',
    'analytics',
    'automations',
    'campaigns',
    'contents',
    'core',
    'integrations',
    'social',
    'UserAccount',
    'status',
]

# Middleware configuration
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]


# Root URL configuration module
ROOT_URLCONF = 'syncfloww.urls'

# Template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  #' Template directories
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


AUTH_USER_MODEL = "UserAccount.User"

# WSGI application callable
WSGI_APPLICATION = 'syncfloww.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# supabase_url = os.environ.get("SUPABASE_URL")
# supabase_key = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(supabase_url, supabase_key)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': '5432',
    }
}


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

# EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'myappsa9@gmail.com'
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = 'no-reply@syncflow.com'

# CORS allowed origins for cross-origin requests
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "https://syncfloww-backend.onrender.com",
    "https://syncfloww.onrender.com",
    "http://localhost:3000",   # keep if you also dev locally
    "http://localhost:5173",
    "https://preview--prompt-reach-ai.lovable.app"
]

CORS_ALLOW_CREDENTIALS = True

# Trusted origins for CSRF protection
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "https://syncfloww-backend.onrender.com",
    "https://syncfloww.onrender.com",
    "http://localhost:3000",   # keep if you also dev locally
    "http://localhost:5173",
    "https://preview--prompt-reach-ai.lovable.app",
]

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"


# Site ID for django.contrib.sites
SITE_ID = 1

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

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


# Social authentication configurations imported from social_config module
SOCIAL_AUTH_CONFIGS = SOCIAL_AUTH_CONFIGS

# Hugging Face API key and model configuration
HUGGINGFACE_API_KEY = env('HUGGINGFACE_API_KEY')
HUGGINGFACE_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Default large language model providers configuration
DEFAULT_LLM_PROVIDERS = [
    {
        'name': 'HuggingFace',
        'provider_class': 'automations.providers.huggingface.HuggingFaceProvider',
        'api_key_env': env('HUGGINGFACE_API_KEY'),
        'base_url': 'https://api-inference.huggingface.co'
    },
    {
        'name': 'OpenAI',
        'provider_class': 'automations.providers.openai.OpenAIProvider',
        'api_key_env': 'OPENAI_API_KEY',
        'base_url': 'https://api.openai.com/v1'
    }
]

CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ("'self'",),
        "connect-src": (
            "'self'",
            "https://syncfloww-backend-w4pw.onrender.com",
            "https://api-inference.huggingface.co",
            "https://api.openai.com",
            "http://localhost:8000",
            "http://localhost:8080",
            "https://preview--prompt-reach-ai.lovable.app",
        ),
        "font-src": ("'self'", "https://fonts.gstatic.com"),
        "img-src": ("'self'", "data:", "https://your-cdn.com"),
        "script-src": (
            "'self'",
            "https://cdn.jsdelivr.net",
            "https://unpkg.com",
            "'unsafe-inline'",  # ⚠️ Avoid in production if possible
        ),
        "style-src": (
            "'self'",
            "https://fonts.googleapis.com",
            "'unsafe-inline'",  # ⚠️ Avoid if possible
        ),
    }
}



AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.apple.AppleIdAuth',
    'social_core.backends.open_id.OpenIdAuth',
    'django.contrib.auth.backends.ModelBackend',
)


ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # disable during dev
ACCOUNT_EMAIL_REQUIRED = True


SOCIAL_AUTH_URL_NAMESPACE = 'social_auth'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =  env('GOOGLE_OAUTH2_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_OAUTH2_CLIENT_SECRET')
SOCIAL_AUTH_GOOGLE_SCOPE = ['email', 'profile']


SOCIAL_AUTH_FACEBOOK_KEY = env('FACEBOOK_APP_ID')
SOCIAL_AUTH_FACEBOOK_SECRET = env('FACEBOOK_APP_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile']

# SOCIAL_AUTH_APPLE_ID = env('APPLE_CLIENT_ID')
# SOCIAL_AUTH_APPLE_SECRET = env('APPLE_CLIENT_SECRET')
  # replace with env var in production

# Authentication classes
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "UserAccount.authentication.CustomUserAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),

}
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social.social_pipeline.associate_brand',  # <-- custom step
    'core.pipeline.bind_brand'
)

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


