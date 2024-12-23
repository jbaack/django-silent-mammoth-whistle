from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner' # https://github.com/bradmontgomery/django-rainbowtests

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "silent_mammoth_whistle",
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
	'silent_mammoth_whistle.middleware.SilentMammothWhistleMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
		'APP_DIRS': True,
    }
]