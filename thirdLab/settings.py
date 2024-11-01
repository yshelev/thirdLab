from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-hiv%coo=76+b^7_f5mu_(b)j*n7#%gecx8hh)i*@4&$%zy+7_s'

DEBUG = True

ALLOWED_HOSTS = []


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'social_django',
    'csgorun',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.steam.SteamOpenId',
    'django.contrib.auth.backends.ModelBackend',
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_STEAM_API_KEY = 'BCC74E0CB3E21FBA4383130F2D2E22AB'
SOCIAL_AUTH_STEAM_EXTRA_DATA = ['player']

AUTH_USER_MODEL = 'csgorun.User'
SOCIAL_AUTH_USER_MODEL = 'csgorun.User'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',

    'social_core.pipeline.social_auth.social_uid',

    'social_core.pipeline.social_auth.auth_allowed',

    'social_core.pipeline.social_auth.social_user',

    'csgorun.pipeline.associate_existing_user',

    'csgorun.pipeline.get_username',

    'social_core.pipeline.user.create_user',

    'social_core.pipeline.social_auth.associate_user',

    'social_core.pipeline.social_auth.load_extra_data',

    'csgorun.pipeline.user_details',
)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'thirdLab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
	    ,
        'APP_DIRS': True,
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


WSGI_APPLICATION = 'thirdLab.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Vladivostok'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
