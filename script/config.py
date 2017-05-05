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
USE_GCLOUD = True

if USE_GCLOUD:
    # Google Cloud Project ID.
    CLOUD_PROJECT_ID = 'opendata-cw2-166700'

    # Google Cloud API key
    CLOUD_API_KEY = 'AIzaSyDubq5gCNwyhQ48XZDgcGxjAPEVn_hVjY0'

    # Google Cloud Auth client id
    GLOUD_AUTH_CLIENT_ID = ''

    # Google Cloud mysql
    CLOUDSQL_USER = 'root'
    CLOUDSQL_PASSWORD = '1qaz2wsx'
    CLOUDSQL_DATABASE = 'proj_db'
    CLOUDSQL_CONNECTION_NAME = 'opendata-cw2-166700:proj-db'

    # Google Cloud database uri
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@/{database}?unix_socket=/cloudsql/{connection_name}').format(
        user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD, database=CLOUDSQL_DATABASE,
        connection_name=CLOUDSQL_CONNECTION_NAME)

    # Google Cloud Storage and upload settings.
    CLOUD_STORAGE_BUCKET = 'opendata-cw2'
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    CLOUD_IMAGE_FOLDER = 'imgs'
    DEFAULT_PROFILE_IMG = 'https://res.citymaps.io/images/web/avatar_default.png'


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
