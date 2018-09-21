import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # App configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or "very-secret-key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    ELASTICSEARCH_URL = 'http://localhost:9200'

    # App Constants
    POSTS_PER_PAGE = 15
