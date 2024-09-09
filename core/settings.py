import os, sys
from pathlib import Path
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

#informa pasta de apps para o django
APPS_DIR = os.path.join(BASE_DIR,'apps')
sys.path.insert(0, APPS_DIR)

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1']

ALLOWED_HOSTS = []

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_APPS = [
]
PROJECT_APPS = [
    'apps.base',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'requestlogs.middleware.RequestLogsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'apps/base/templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DBNAME'),
		'USER': os.getenv('DBUSER'),
		'PASSWORD': os.getenv('DBPASSWORD'),
        'HOST': os.getenv('DBHOST'),
        'PORT': os.getenv('DBPORT'),
    }
}

# password validation
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
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# configuração de arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'apps/base/static')
]

#configuração de media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#configuração de logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requestlogs_to_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
        },
    },
    'loggers': {
        'requestlogs': {
            'handlers': ['requestlogs_to_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
REQUESTLOGS = {
    'STORAGE_CLASS': 'requestlogs.storages.LoggingStorage',
    'ENTRY_CLASS': 'requestlogs.entries.RequestLogEntry',
    'SECRETS': ['password', 'token'],
    'ATTRIBUTE_NAME': '_requestlog',
    'METHODS': ('GET', 'PUT', 'PATCH', 'POST', 'DELETE'),
    'JSON_ENSURE_ASCII': True,
    'IGNORE_USER_FIELD': None,
    'IGNORE_USERS': [],
    'IGNORE_PATHS': None,
}

#configuração de cors
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
CORS_ALLOW_HEADERS = (
	*default_headers,
    'X-Register',
)

#segurança - modo não debug (produção)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    ADMINS = [
        (os.getenv('SUPERUSER')),
        (os.getenv('EMAIL')),
    ]
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

#configuração de email
EMAIL_HOST=os.getenv('EMAIL_HOST'),
EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER'),
EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD'),
EMAIL_PORT=os.getenv('EMAIL_PORT'),
EMAIL_USE_TLS=os.getenv('EMAIL_USE_TLS', 'False').lower() in ['true', '1']
DEFAULT_FROM_EMAIL=os.getenv('DEFAULT_FROM_EMAIL'),
SERVER_EMAIL=os.getenv('SERVER_EMAIL'),