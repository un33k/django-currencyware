DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "un33k"
INSTALLED_APPS = ['currencyware']
MIDDLEWARE_CLASSES = []
PRIORITY_CURRENCY_CODES = ['CAD']