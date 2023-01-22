from dotenv import load_dotenv
import os

from .common_settings import *

load_dotenv(".env")
settings = os.getenv('SETTINGS')

if settings == "prod":
    print("PRODUCTION SERVER")
    DEBUG = False

    ALLOWED_HOSTS = ["sasthrayaan.cusat.ac.in", "sasthrayaan.cusat.me"]
    cors_allowed_origins = ["https://sasthrayaan.cusat.ac.in", "https://sasthrayaan.cusat.me"]
    CSRF_TRUSTED_ORIGINS = cors_allowed_origins

    STATIC_ROOT = os.getenv('STATIC_ROOT')
    MEDIA_ROOT = os.getenv('MEDIA_ROOT')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

else:
    print("DEV SERVER")
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
