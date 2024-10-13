# Django settings for Social_Media_Project project.

# Generated by 'django-admin startproject' using Django 5.0.6.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.0/ref/settings/


from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import environ
env = environ.Env()
environ.Env.read_env() 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#nx$+v^74ywz))md8p3@2z^e^5-fzb^3xvfao(qn+5-ncojomx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app"]
# ALLOWED_HOSTS = ["127.0.0.1", "https://social-2nd-project-backend.vercel.app"]

# Application definition

INSTALLED_APPS = [

    "whitenoise.runserver_nostatic",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  #cors
    'Auth_System',
    'POST_CRUD',

    'rest_framework',
    'rest_framework.authtoken',  # For Token-based Authentication

    'cloudinary',
    'cloudinary_storage', #cloudinary add korlam
]
# AUTH_USER_MODEL = 'Auth_System.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  #cors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',
    # "https://2nd-project-frontend.vercel.app",
    "https://frontofsocial-avoata0nc-md-jubaer-mahmud-sarkers-projects.vercel.app",

]
CSRF_TRUSTED_ORIGINS = [
    "https://social-2nd-project-backend.vercel.app",
    # "https://social-2nd-project-backend-72na3ocnx.vercel.app",
    'http://127.0.0.1:5500',  # Frontend running locally 
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

WSGI_APPLICATION = 'Social_Media_Project.wsgi.app'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.kjbdgbdulkunsvgzmgwp',
        'PASSWORD': 'F9rId9xGlXAV81WH',
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '6543'
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
# settings.py
IMGBB_API_KEY = '59c029e1206724ae1f2e3c30d278d10f'  
CLOUDINARY_URL = 'cloudinary://982385273458864:vLcqLJs2hQWgCwIqbG82drNQuzs@doxrbnaqy'

# Add your Cloudinary credentials
# cloudinary.config( 
#   cloud_name = "doxrbnaqy", 
#   api_key = "982385273458864", 
#   api_secret = "vLcqLJs2hQWgCwIqbG82drNQuzs" 
# )

# Ensure that the `CLOUDINARY_URL` environment variable is set in your `.env` file or directly in `settings.py`
# CLOUDINARY_URL = 'cloudinary://982385273458864:vLcqLJs2hQWgCwIqbG82drNQuzs@doxrbnaqy'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
