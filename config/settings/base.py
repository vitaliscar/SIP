# Configuración base para el proyecto

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicaciones personalizadas
    'apps.users',
    'apps.clients',
    'apps.products',
    'apps.sales',
    'apps.goals',
    'apps.reporting',
    'apps.ai_models',
    'apps.core',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sales_intelligence',  # ← cámbialo de 'SIP' a 'postgres'
        'USER': 'postgres',
        'PASSWORD': 'Joaquin.0305.',
        'HOST': 'localhost',
        'PORT': '5432',  # Asegúrate de que sea el correcto
    }
}


LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'
