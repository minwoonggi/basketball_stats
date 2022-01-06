from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'basketball_stats',
        'USER': 'root',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
SECRET_KEY = 'django-insecure-&!hsmydmi2^0zwz8@0epx8*0_a#sg1@gh49*ny6&f(+ywc&uai'