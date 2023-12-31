import os

APP_ENV = os.environ.get('APP_ENV')
DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_NAME = os.environ.get('MYSQL_DATABASE')
STATIC_URL = os.environ.get('STATIC_URL')
ALLOW_ORIGIN = os.environ.get('ALLOW_ORIGIN')
