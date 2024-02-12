"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / 'templates'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v$dz*@o!%+&vir9^#ls)7m+pl$)e-)7b56y=^xg58)r3m6ps)x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.0.110.209']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # comunes al proyecto
    'core.common',
    'core.modal',    
    'core.users',

    # mis aplicaciones
    'apps.home',
    'apps.entidades',
    'apps.recepcion',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'config.wsgi.application'


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
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'staticroot/'


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static'),
    BASE_DIR / 'static',
    'core/users/static',
)

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# -------------------------------------------------------------------
# redirecciona a home al realizar un login exitoso
# -------------------------------------------------------------------
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/accounts/logout/'
LOGOUT_REDIRECT_URL = '/'



# -------------------------------------------------------------------
# grapelli (personalización de site admin) debe ir antes de cualquier otra app
# -------------------------------------------------------------------
# INSTALLED_APPS = ['grappelli'] + INSTALLED_APPS


# -------------------------------------------------------------------
# configuración para django-crispy-forms
# -------------------------------------------------------------------
INSTALLED_APPS += ['crispy_forms','crispy_bootstrap4']
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# -------------------------------------------------------------------
# configuración para django-table
# -------------------------------------------------------------------
INSTALLED_APPS += ['django_tables2',]


# -------------------------------------------------------------------
# configuración para django-table
# -------------------------------------------------------------------
INSTALLED_APPS += ['django_filters',]


# -------------------------------------------------------------------
# configuración para django-select2
# -------------------------------------------------------------------
INSTALLED_APPS += ['django_select2']


# # -------------------------------------------------------------------
# # configuración para django-smart-selects
# # -------------------------------------------------------------------
# INSTALLED_APPS += ['smart_selects',]
# # JQUERY_URL = True
# USE_DJANGO_JQUERY = True


# -------------------------------------------------------------------
# configuración para debug
# -------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar',]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}



# # -------------------------------------------------------------------
# # visualiza todas las consultas SQL por consula
# # muy bueno para realizar depuración desde la consola
# # -------------------------------------------------------------------
# if DEBUG:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'level': 'DEBUG',
#                 'class': 'logging.StreamHandler',
#             }
#         },
#         'loggers': {
#             'django.db.backends': {
#                 'handlers': ['console'],
#                 'level': 'DEBUG',
#             },
#         }
#     }
