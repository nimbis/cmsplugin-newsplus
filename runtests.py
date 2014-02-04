import sys
from os.path import join, dirname

from django.conf import settings


def get_test_runner():
    # This code is based on the new test-setup in django-cms 2.3
    # https://raw.github.com/divio/django-cms/
    # 595d9092d95ceb45ae666b78a86a4c71ed395396/cms/test_utils/cli.py
    settings.configure(
        CACHE_BACKEND='locmem:///',
        DEBUG=True,
        TEMPLATE_DEBUG=True,
        DATABASE_SUPPORTS_TRANSACTIONS=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        SITE_ID=1,
        USE_I18N=True,
        MEDIA_ROOT='/media/',
        STATIC_ROOT='/static/',
        CMS_MEDIA_ROOT='/cms-media/',
        CMS_MEDIA_URL='/cms-media/',
        MEDIA_URL='/media/',
        STATIC_URL='/static/',
        ADMIN_MEDIA_PREFIX='/static/admin/',
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        SECRET_KEY='key',
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
        ),
        TEMPLATE_CONTEXT_PROCESSORS=[
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.i18n",
            "django.core.context_processors.debug",
            "django.core.context_processors.request",
            "django.core.context_processors.media",
            'django.core.context_processors.csrf',
            "cms.context_processors.media",
            "sekizai.context_processors.sekizai",
            "django.core.context_processors.static",
        ],
        MIDDLEWARE_CLASSES=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'cms.middleware.multilingual.MultilingualURLMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.doc.XViewMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'cms.middleware.user.CurrentUserMiddleware',
            'cms.middleware.page.CurrentPageMiddleware',
            'cms.middleware.toolbar.ToolbarMiddleware',
        ],
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.staticfiles',
            'cms',
            'menus',
            'mptt',
            'cms.plugins.text',
            'cms.plugins.picture',
            'cms.plugins.file',
            'cms.plugins.flash',
            'cms.plugins.link',
            'cms.plugins.snippet',
            'cms.plugins.googlemap',
            'cms.plugins.teaser',
            'cms.plugins.video',
            'cms.plugins.twitter',
            'cms.plugins.inherit',
            'south',
            'sekizai',
            'cmsplugin_newsplus',
        ],
        LANGUAGE_CODE="en",
        LANGUAGES=(
            ('en', 'English'),
            ('de', 'German'),
        ),
        CMS_LANGUAGES=(
            ('en', 'English'),
            ('de', 'German'),
        ),
        CMS_LANGUAGE_CONF={
            'de': ['de', 'en'],
            'en': ['de', 'de'],
        },
        CMS_SOFTROOT=True,
        CMS_MODERATOR=True,
        CMS_PERMISSION=True,
        CMS_CACHE_DURATIONS={
            'menus': 0,
            'content': 0,
            'permissions': 0,
        },
        CMS_URL_OVERWRITE=True,
        SOUTH_TESTS_MIGRATE=False,
        JUNIT_OUTPUT_DIR='.',
        TIME_TESTS=True,
        CMS_TEMPLATES=[('test_template.html', 'base')],
        TEMPLATE_DIRS=[join(dirname(__file__), 'test_setup', 'templates')],
        ROOT_URLCONF='cmsplugin_newsplus.urls'
    )
    from south.management.commands import patch_for_test_db_setup
    patch_for_test_db_setup()
    from django.test.utils import get_runner
    return get_runner(settings)


def main():
    test_runner = get_test_runner()(verbosity=1, interactive=False)
    failures = test_runner.run_tests(['cmsplugin_newsplus'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    main()
