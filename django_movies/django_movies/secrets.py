
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*(da@pheg1u8-98vp3d69!^jb5m*ht&3+my=%!qn&$+b)4$w$j'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movies',
        'USER': 'hrumba',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
