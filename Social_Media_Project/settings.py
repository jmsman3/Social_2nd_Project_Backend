# Django settings for Social_Media_Project project.

from pathlib import Path
import environ

# Environment variable configuration
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = env("SECRET_KEY")  # Use an environment variable for the secret key
DEBUG = env.bool("DEBUG", default=False)  # Set DEBUG from environment variables

# Specify allowed hosts
ALLOWED_HOSTS = [
    '127.0.0.1',  # Localhost for development
    '.vercel.app',  # Allow all subdomains of vercel.app
    'social-2nd-project-backend.vercel.app',  # Your production domain
]

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = False  # Set to False for security
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',  # Local frontend
    "https://frontofsocial-avoata0nc-md-jubaer-mahmud-sarkers-projects.vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://social-2nd-project-backend.vercel.app",
    'http://127.0.0.1:5500',  # Frontend running locally 
]

# Application definition
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # CORS
    'Auth_System',
    'POST_CRUD',
    'rest_framework',
    'rest_framework.authtoken',  # For Token-based Authentication
    'cloudinary',
    'cloudinary_storage',  # Cloudinary
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]

CORS_ALLOW_HEADERS = [
    'content-type',
    'Authorization',
    'X-CSRFToken',
    'X-Requested-With',
]

ROOT_URLCONF = 'Social_Media_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Social_Media_Project.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME", default='postgres'),
        'USER': env("DB_USER", default='postgres.kjbdgbdulkunsvgzmgwp'),
        'PASSWORD': env("DB_PASSWORD", default='F9rId9xGlXAV81WH'),
        'HOST': env("DB_HOST", default='aws-0-ap-southeast-1.pooler.supabase.com'),
        'PORT': env("DB_PORT", default='6543')
    }
}

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

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'
MEDIA_URL = '/media/'

# Cloudinary configuration
IMGBB_API_KEY = env("IMGBB_API_KEY")  # Load from environment
CLOUDINARY_URL = env("CLOUDINARY_URL")  # Load from environment

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email backend configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
