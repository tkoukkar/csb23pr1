"""
Django settings for csb23pr1 project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^6+ub#pf+3l1q@-kdxvk6l_fq#%=*5lou*%v@qqbu84+mm!_*b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    # Oops (FLAW 3)
# DEBUG = False    # Fix to the above

ALLOWED_HOSTS = []    # Causes an error when the fix above is applied (ie. when DEBUG = False).
# ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']    # Replace the previous line with this one after applying the fix.


# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Cookie security (FLAW 4)

SESSION_COOKIE_HTTPONLY = False    # Allows cookie theft with JavaScript
# SESSION_COOKIE_HTTPONLY = True    # Fix to the above
# SESSION_COOKIE_AGE = 900
# CSRF_COOKIE_AGE = 900
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # Alternative to the SESSION_COOKIE_AGE fix
                                            # - Pro: Takes effect immediately when user closes their browser
                                            # - Con: Relies on the user actually properly closing their browser > seems fundamentally insecure

# Fixes to logging issues (FLAW 5)
# - More extensive logs (level INFO rather than ERROR), storage in a file rather than email
#
# LOGGING = {
#    "version": 1,
#    "disable_existing_loggers": False,
#    "handlers": {
#        "console": {
#            "class": "logging.StreamHandler",
#        },
#        "file": {
#            "level": "INFO",
#            "class": "logging.FileHandler",
#            "filename": BASE_DIR / "logs/events.log",
#        },
#    },
#    "loggers": {
#        "django": {
#            "handlers": ["console", "file"],
#            "level": "INFO",
#            "propagate": True,
#        },
#    },
#}

ROOT_URLCONF = 'csb23pr1.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'csb23pr1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/polls/'
LOGOUT_REDIRECT_URL = '/polls/'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
