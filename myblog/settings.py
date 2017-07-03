import os



DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
]
ADMINS = (
    ('nazi', '1500256797@qq.com'),
)

MANAGERS = ADMINS
# myblog就是网站目录
# myblog=os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: os.path.join(myblog, ...)
myblog = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blog',
        'USER':'root',
        'PASSWORD':'123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
'''
静态文件头大。
css，JS，图片，html，要怎么配置？

'''

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(myblog, 'static'),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(myblog, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

INSTALLED_APPS = [
    'bootstrap_admin',# 一定要放在'django.contrib.admin'前面
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # 用来管理静态文件（CSS   JS   图片  html ）
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'taggit',
    'contact_form',
    'blog',
    'easy_thumbnails',
    'filer',
    'mptt',


]
# 在处理缩略图的部分，则要在这里加入这样的配置
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.filters',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
)

# 指定文件存放的位置
FILER_PATH = os.path.join(myblog, 'static/')  # 这个位置基本没用
FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(FILER_PATH, 'media/filer'),
                'base_url': '/media/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public'
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(FILER_PATH, 'media/filer_thumbnails'),
                'base_url': '/media/filer_thumbnails/',
            },
        },
    },
}

MEDIA_ROOT = os.path.join(FILER_PATH, 'media')
MEDIA_URL = '/media/'
# Hosts/domain names that are valid for this site; required if DEBUG is False
TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v2x^#lrv$(xp3ost97tbr4wvodd6l6obm_f3s%a^6pdmpxhw=g'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# cache entire site
MIDDLEWARE_CLASSES_ADDITION_FIRST = (
    'django.middleware.cache.UpdateCacheMiddleware',
)

MIDDLEWARE_CLASSES_ADDITION_LAST = (
    'django.middleware.cache.FetchFromCacheMiddleware',
)
ROOT_URLCONF = 'myblog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myblog.wsgi.application'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

