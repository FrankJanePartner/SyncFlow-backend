from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-d8o0!!&od@noufcplg$y65vo*l0_tu#+pe0(2oecme5)b)or9y'

DEBUG = True

ALLOWED_HOSTS = []


SITE_ID=1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # my apps
    'core',

    # third party apps
    'mptt',
    'tinymce',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_countries',
    'phonenumber_field',
    # 'requests-oauthlib',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.discord',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.edx',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.figma',
    # 'allauth.socialaccount.providers.frontier',
    # 'allauth.socialaccount.providers.fxa',
    # 'allauth.socialaccount.providers.gitea',
    'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.gumroad',
    'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.meetup',
    # 'allauth.socialaccount.providers.microsoft',
    # 'allauth.socialaccount.providers.notion',
    # 'allauth.socialaccount.providers.openid_connect',
    # 'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.reddit',
    # 'allauth.socialaccount.providers.shopify',
    # 'allauth.socialaccount.providers.slack',
    # 'allauth.socialaccount.providers.snapchat',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.telegram',
    # 'allauth.socialaccount.providers.trello',
    # 'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.twitter_oauth2',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vimeo_oauth2',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.yahoo',
    # 'allauth.socialaccount.providers.zoom',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # corsheaders specific middleware
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # allauth specific middleware
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'syncflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.brand'
            ],
        },
    },
]

WSGI_APPLICATION = 'syncflow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',  # If using Token Authentication
        'rest_framework.authentication.SessionAuthentication',  # For web session login
        'rest_framework.authentication.BasicAuthentication',  # Optional
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}


SOCIALACCOUNT_PROVIDERS = {
    # 'amazon': {
    #     'APP': {
    #         'client_id': 'YOUR-AMAZON-CLIENT-ID-HERE',
    #         'secret': 'YOUR-AMAZON-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'angellist': {
    #     'APP': {
    #         'client_id': 'YOUR-ANGELLIST-CLIENT-ID-HERE',
    #         'secret': 'YOUR-ANGELLIST-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'digitalocean': {
    #     'APP': {
    #         'client_id': 'YOUR-DIGITALOCEAN-CLIENT-ID-HERE',
    #         'secret': 'YOUR-DIGITALOCEAN-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'discord': {
        'APP': {
            'client_id': 'YOUR-DISCORD-CLIENT-ID-HERE',
            'secret': 'YOUR-DISCORD-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    # 'dropbox': {
    #     'APP': {
    #         'client_id': 'YOUR-DROPBOX-CLIENT-ID-HERE',
    #         'secret': 'YOUR-DROPBOX-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'APP': {
            'client_id': '509697181767177',
            'secret': '651a9335cb086c9c8d5fca07d71f1a86',
            'key': ''
        }
    },
    # 'figma': {
    #     'APP': {
    #         'client_id': 'YOUR-FIGMA-CLIENT-ID-HERE',
    #         'secret': 'YOUR-FIGMA-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'frontier': {
    #     'APP': {
    #         'client_id': 'YOUR-FRONTIER-CLIENT-ID-HERE',
    #         'secret': 'YOUR-FRONTIER-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'fxa': {
    #     'APP': {
    #         'client_id': 'YOUR-FXA-CLIENT-ID-HERE',
    #         'secret': 'YOUR-FXA-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'gitea': {
    #     'APP': {
    #         'client_id': 'YOUR-GITEA-CLIENT-ID-HERE',
    #         'secret': 'YOUR-GITEA-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'github': {
        'APP': {
            'client_id': 'YOUR-GITHUB-CLIENT-ID-HERE',
            'secret': 'YOUR-GITHUB-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    # 'gitlab': {
    #     'APP': {
    #         'client_id': 'YOUR-GITLAB-CLIENT-ID-HERE',
    #         'secret': 'YOUR-GITLAB-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': '699745756873-153o4ff332apu60s7gnj4qf7mtfttofk.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    # 'gumroad': {
    #     'APP': {
    #         'client_id': 'YOUR-GUMROAD-CLIENT-ID-HERE',
    #         'secret': 'YOUR-GUMROAD-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'instagram': {
        'APP': {
            'client_id': '1812151136033639',
            'secret': '348f0f1e8cad793b845e3bed44f6e55f',
            'key': ''
        }
    },
    'linkedin_oauth2': {
        'APP': {
            'client_id': 'YOUR-LINKEDIN-CLIENT-ID-HERE',
            'secret': 'YOUR-LINKEDIN-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    # 'meetup': {
    #     'APP': {
    #         'client_id': 'YOUR-MEETUP-CLIENT-ID-HERE',
    #         'secret': 'YOUR-MEETUP-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'microsoft': {
    #     'APP': {
    #         'client_id': 'YOUR-MICROSOFT-CLIENT-ID-HERE',
    #         'secret': 'YOUR-MICROSOFT-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'notion': {
    #     'APP': {
    #         'client_id': 'YOUR-NOTION-CLIENT-ID-HERE',
    #         'secret': 'YOUR-NOTION-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'openid_connect': {
    #     'APP': {
    #         'client_id': 'YOUR-OPENID-CLIENT-ID-HERE',
    #         'secret': 'YOUR-OPENID-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'pinterest': {
    #     'APP': {
    #         'client_id': 'YOUR-PINTEREST-CLIENT-ID-HERE',
    #         'secret': 'YOUR-PINTEREST-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'reddit': {
        'APP': {
            'client_id': 'YOUR-REDDIT-CLIENT-ID-HERE',
            'secret': 'YOUR-REDDIT-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    # 'shopify': {
    #     'APP': {
    #         'client_id': 'YOUR-SHOPIFY-CLIENT-ID-HERE',
    #         'secret': 'YOUR-SHOPIFY-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'slack': {
    #     'APP': {
    #         'client_id': 'YOUR-SLACK-CLIENT-ID-HERE',
    #         'secret': 'YOUR-SLACK-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'snapchat': {
    #     'APP': {
    #         'client_id': 'YOUR-SNAPCHAT-CLIENT-ID-HERE',
    #         'secret': 'YOUR-SNAPCHAT-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'soundcloud': {
    #     'APP': {
    #         'client_id': 'YOUR-SOUNDCLOUD-CLIENT-ID-HERE',
    #         'secret': 'YOUR-SOUNDCLOUD-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'spotify': {
    #     'APP': {
    #         'client_id': 'YOUR-SPOTIFY-CLIENT-ID-HERE',
    #         'secret': 'YOUR-SPOTIFY-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'telegram': {
        'APP': {
            'client_id': 'YOUR-TELEGRAM-CLIENT-ID-HERE',
            'secret': 'YOUR-TELEGRAM-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    # 'twitch': {
    #     'APP': {
    #         'client_id': 'YOUR-TWITCH-CLIENT-ID-HERE',
    #         'secret': 'YOUR-TWITCH-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    'twitter': {
        'APP': {
            'client_id': 'YOUR-TWITTER-CLIENT-ID-HERE',
            'secret': 'YOUR-TWITTER-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    'twitter_oauth2': {
        'APP': {
            'client_id': 'YOUR-TWITTER-OAUTH2-CLIENT-ID-HERE',
            'secret': 'YOUR-TWITTER-OAUTH2-CLIENT-SECRET-HERE',
            'key': ''
        }
    },
    # 'vimeo': {
    #     'APP': {
    #         'client_id': 'YOUR-VIMEO-CLIENT-ID-HERE',
    #         'secret': 'YOUR-VIMEO-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'vimeo_oauth2': {
    #     'APP': {
    #         'client_id': 'YOUR-VIMEO-OAUTH2-CLIENT-ID-HERE',
    #         'secret': 'YOUR-VIMEO-OAUTH2-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'vk': {
    #     'APP': {
    #         'client_id': 'YOUR-VK-CLIENT-ID-HERE',
    #         'secret': 'YOUR-VK-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'yahoo': {
    #     'APP': {
    #         'client_id': 'YOUR-YAHOO-CLIENT-ID-HERE',
    #         'secret': 'YOUR-YAHOO-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
    # 'zoom': {
    #     'APP': {
    #         'client_id': 'YOUR-ZOOM-CLIENT-ID-HERE',
    #         'secret': 'YOUR-ZOOM-CLIENT-SECRET-HERE',
    #         'key': ''
    #     }
    # },
}


# AUTH_USER_MODEL = 'accounts.CustomUser'
# ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.custom_forms.CustomSignupForm'

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
# }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True #change if using SSL (465)
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'myappsa9@gmail.com'
EMAIL_HOST_PASSWORD = 'xlxd lcka gqed pngs'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'



CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    "http://localhost:8082",
    "http://127.0.0.1:8082",
]

CORS_ALLOW_ALL_ORIGINS = True

DJREST_AUTH = {
    'USE_JSON': True,
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'REGISTER_SERIALIZER': 'dj_rest_auth.registration.serializers.RegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'VERIFICATION_URL': '/api/auth/verify-email/',
}


LOGIN_URL = '/accounts/login/'
SIGNUP_URL = '/accounts/signup/'
LOGIN_REDIRECT_URL = '/dashboard/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_LOGIN_METHODS = {'email', 'username'}
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SIGNUP_FIELDS = ['email*', 'first_name*', 'last_name*', 'password1*', 'password2*']

ACCOUNT_EMAIL_SUBJECT_PREFIX = "SyncFlow "
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/accounts/login/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/dashboard/"


# REST_USE_JWT = True  # if you're using JWT

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
