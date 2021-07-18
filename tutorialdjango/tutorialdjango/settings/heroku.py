# import environ
# from tutorialdjango.settings.base import *

# # env = environ.Env(
# #     # set casting, default value
# #     DEBUG=(bool, False)
# # )
# env = environ.Env()
# # reading .env file
# environ.Env.read_env()

# # False if not in os.environ
# # DEBUG = env('DEBUG')
# DEBUG = env.bool("DEBUG", False)

# # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY')

# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# # Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
# DATABASES = {
#     # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
#     'default': env.db(),
#     # read os.environ['SQLITE_URL']
#     'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
# }

# CACHES = {
#     # read os.environ['CACHE_URL'] and raises ImproperlyConfigured exception if not found
#     'default': env.cache(),
#     # read os.environ['REDIS_URL']
#     'redis': env.cache('REDIS_URL')
# }

import environ

from tutorialdjango.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}