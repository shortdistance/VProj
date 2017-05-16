# -*- coding: utf-8 -*-
# Project Name
PROJECT_NAME = 'opendata-cw2'

# Determine system whether start with debug mode
DEBUG = True

# Cookie security key
SECRET_KEY = 'AIzaSyAlpjgnmPOM99xvTK_KzGCvVWLMXC_MaA0'
# Session timeout time
SESSION_TIMEOUT = 60 * 60

# Use google cloud or not
USE_GCLOUD = False
if USE_GCLOUD:
    # Google Cloud Project ID.
    CLOUD_PROJECT_ID = 'opendata-cw2-166700'

    # Google Cloud API key
    CLOUD_API_KEY = 'AIzaSyDubq5gCNwyhQ48XZDgcGxjAPEVn_hVjY0'

    # Google Cloud Auth client id
    GLOUD_AUTH_CLIENT_ID = '530820680296-n63so4mi7domecctilbi3630108r7e0s.apps.googleusercontent.com'

    # Google Cloud mysql
    CLOUDSQL_USER = 'root'
    CLOUDSQL_PASSWORD = '1qaz2wsx'
    CLOUDSQL_IP = '104.197.148.223'
    CLOUDSQL_DATABASE = 'proj_db'
    CLOUDSQL_CONNECTION_NAME = 'opendata-cw2-166700:us-central1:projdb'

    # Google Cloud database uri
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@{ip}:3306/{database}?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD, ip=CLOUDSQL_IP, database=CLOUDSQL_DATABASE,
        connection_name=CLOUDSQL_CONNECTION_NAME)

    # Google Cloud Storage and upload settings.
    CLOUD_STORAGE_BUCKET = 'opendata-cw2'

else:
    # Local mysql
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_NAME = 'projdb'
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@{host}:{port}/{database}').format(
        user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT,
        database=DB_NAME)

# Record number displayed in single page.
PAGESIZE = 20

# the flag whether open email notification
ENABLE_MAIL_NOTICE = False

# the host of mail server
SMTP_HOST = 'smtp.163.com'

# default sender
EMAIL_SENDER = 'zhanglei520vip@163.com'

# the password of default sender
SENDER_PASS = '1qaz2wsx'

# email subject prefix
MAIL_SUBJECT_PREFIX = '[' + PROJECT_NAME.capitalize() + ']'

# The max distance between users can be found
MAX_FOUND_DISTANCE_BETWEEN_USERS = 2000

ZOOPLER_KEY = 'hkcbz38j32pqgepepv7nx5vu'