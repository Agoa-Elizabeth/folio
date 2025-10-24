import os
from pathlib import Path
import dj_database_url

print("=== RENDER ENV VARIABLE ===")
print(f"RENDER in os.environ: {'RENDER' in os.environ}")
print(f"RENDER value: {os.environ.get('RENDER', 'NOT SET')}")
print("===========================")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # FIXED: Uncommented this
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myportfolio.wsgi.application'

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files - FIXED CONFIGURATION
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Check if static directory exists before adding to STATICFILES_DIRS
portfolio_static = BASE_DIR / "portfolio" / "static"
STATICFILES_DIRS = []
if portfolio_static.exists():
    STATICFILES_DIRS.append(portfolio_static)

# WhiteNoise storage for compression and caching
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'elizabethagoa@gmail.com'
EMAIL_HOST_PASSWORD = 'hkcw cmip rsfg mbiq'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Environment-specific settings
if 'RENDER' in os.environ:
    # Production settings for Render
    print("=== PRODUCTION SETTINGS ACTIVATED ===")
    DEBUG = False  
    
    # Use actual domain names
    ALLOWED_HOSTS = [
        'folio-5-4345.onrender.com',
        '.onrender.com',
    ]
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-for-production')
    
    # Database configuration for production
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        DATABASES = {
            'default': dj_database_url.config(
                default=database_url,
                conn_max_age=600,
                conn_health_checks=True,
            )
        }
    else:
        # Fallback to SQLite if no DATABASE_URL (not recommended for production)
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
else:
    # Local development settings
    print("=== DEVELOPMENT SETTINGS ACTIVE ===")
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    SECRET_KEY = 'django-insecure-%f)p0)cf3hc$w(aso6ff&5azjk+m30t6f(748k_&xh^7z!ex+a'
    
    # Database for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }