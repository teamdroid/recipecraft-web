# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

#DB Settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NameOfDB',
        'USER': 'login',
        'PASSWORD': 'password',
        'HOST': '172.**.**.58',
        'PORT': '80',
    }
}