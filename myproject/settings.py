"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0)b1)!s5f--&zej4&=-ydpc+nwwq4)*d69hd(u&@4*ul4mib()'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  #현재 우리 사이트 관련된 정보를 다루기 위해서 추가해줬습니다.
    
    #Django 소셜 로그인 관련 App
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    #카카오(다른 서비스의 소셜로그인 사용시 다른 서비스 등록해줘야함.)
    'allauth.socialaccount.providers.kakao',

    'memo',
    'accounts',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko' #프로젝트의 언어셋팅을 한글로 바꿉니다.

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/' #사용자가 STATIC파일을 요청할 URL
STATIC_ROOT = BASE_DIR / 'static' #앱별로 흩어진 Static파일들을 해당 경로에 모아줌(python manage.py collectstatic)
# 사용자는 STATIC_URL의 경로로 요청하게되고 우리는 그 장소에 static 요소들을 준비해둔다. 
# 그래서 STATIC_URL 이랑 STATIC_ROOT의 위치는 일치시켜주자.
# 개발할때는 runserver 명령어 실행시 내부적으로 collectstatic와 같은 동작을 수행함.
# 따라서 STATIC_ROOT는 개발시에는 굳이 필요없지만 나중에 배포시에는 runserver명령어를 실행할게 아니므로, 명시적으로 collectstatic을 해줘야하고
# 이를 위해서 STATIC_ROOT도 작성해줘야한다.

STATICFILES_DIRS = [
    BASE_DIR / "basestatic",
]
# 프로젝트 폴더 밑에 basestatic이라는 폴더를 하나 만들어주고 base.css를 추가적으로 작성해서 관리하고있습니다.
# 해당 폴더는 새로 만들어 준 폴더이므로 STATIC_FILE을 관리하는 FINDER가 해당 폴더도 인지하고 모아줄 수 있게 등록을 해주는 과정입니다.

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 여기서 BASE_DIR은 프로젝트 폴더를 의미합니다.

LOGIN_REDIRECT_URL = '/' #로그인 후 REDIRECT경로를 설정하는데
                         #따로 설정하지 않으면 Profile페이지를 찾아갑니다.
LOGOUT_REDIRECT_URL = '/'


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
#기존 Django model과의 호환을 위해서 설정해준다.



SITE_ID = 1   #admin page에서 '사이트틀' 부분에서 example.com을 수정해서 우리의 domain주소로 바꿔 줬기때문에
              #SITE_ID가 1번이고, 만약에 admin site에서 사이트틀 내부의 정보를 지우고 추가 생성해준거라면 추가생성한 정보의 ID값과 일치시켜줘야한다.

