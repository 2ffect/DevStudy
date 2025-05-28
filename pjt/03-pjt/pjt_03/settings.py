# myproject/settings.py

from pathlib import Path

# 기존 설정들...
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-l-lr4ve3m8)d$*jdzx(s&5y0u(hxiovv-0^)ww=ciop^#096rb'
DEBUG = True  # 개발 환경에서는 True로 설정 (배포 시 False로 설정해야 함)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # 로컬 개발용 호스트 설정

# Application definition
INSTALLED_APPS = [
    'finance',
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

ROOT_URLCONF = 'pjt_03.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'pjt_03.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # 정적 파일 URL 경로

# 프로젝트 내 static 디렉토리 추가
STATICFILES_DIRS = [
    BASE_DIR / "finance" / "static",  # 'finance/static' 폴더 추가
]

# 배포 환경에서는 collectstatic을 통해 정적 파일을 모을 디렉토리 설정
STATIC_ROOT = BASE_DIR / "staticfiles"  # 예시: staticfiles 폴더로 모음

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


