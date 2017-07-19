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
SQLALCHEMY_DATABASE_URI = 'sqlite:///projdb.sqlite'

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

# channel coast api key
CHANNNEL_COAST_API_KEY = 'dfjn4ty1jdpm5qrgc6jwpdmk9gh7gf6u'

CHANNNEL_COAST_API_KEY = 'dfjn4ty1jdpm5qrgc6jwpdmk9gh7gf6u'

RABBITMQ_BIGWIG_URL = 'amqp://1G8enNXO:Nf_uWwcyHBs-jg3UhAkRskXZSLwh7ppq@sad-nelthilta-30.bigwig.lshift.net:11020/hOM1ppDgFf6w'

REDIS_URL = 'redis://h:p550d645fdb271552914055f59b174ec1e33475a443ad4aff1be2ad41c935f2da@ec2-34-226-55-20.compute-1.amazonaws.com:28949'

MONGODB_URI = 'mongodb://heroku_3gr09dlh:ohb0regig4p4bsphgktn25llge@ds113063.mlab.com:13063/heroku_3gr09dlh'

SECONDS = 900
