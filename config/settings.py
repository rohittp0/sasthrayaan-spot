from dotenv import load_dotenv
import os

load_dotenv(".env")
settings = os.getenv('SETTINGS')

if settings == "prod":
    print("PRODUCTION SERVER")
    DEBUG = False
    from .common_settings import *

    ALLOWED_HOSTS = ["sasthrayaan.cusat.ac.in", "sasthrayaan.cusat.me"]
    cors_allowed_origins = ["https://ssasthrayaan.cusat.ac.in", "https://ssasthrayaan.cusat.me"]
    CSRF_TRUSTED_ORIGINS = cors_allowed_origins + ALLOWED_HOSTS

    STATIC_ROOT = "/var/www/html/static/"
    MEDIA_ROOT = '/var/www/html/media'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:
    print("DEV SERVER")
    DEBUG = True
    from .common_settings import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
