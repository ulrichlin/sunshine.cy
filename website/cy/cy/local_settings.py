DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cy', # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gully45t$pha@!dx8@a)1vg9jt!gd**wnr48_5uv(^h1n191nj'
