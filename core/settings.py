from pathlib import Path
import os 
from dotenv import load_dotenv

# ========================================
# BASE CONFIGURATION
# ========================================

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-4)1a-e_+7ys4$^7x*$xuvlu8!q1400_8*lfkds10@nvk(o31bk')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = []

# ========================================
# APPLICATION DEFINITION
# ========================================

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Local apps
    'authcore',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
SITE_ID = 1

# ========================================
# TEMPLATES
# ========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========================================
# DATABASE
# ========================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# ========================================
# AUTHENTICATION
# ========================================

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Django Allauth custom behavior
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/manage_profiles/'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_LOGIN_ON_SIGNUP = False

# ========================================
# INTERNATIONALIZATION
# ========================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ========================================
# STATIC FILES
# ========================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'statics']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ========================================
# DEFAULTS
# ========================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
