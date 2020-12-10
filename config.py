import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='cynde'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    MAIL_USERNAME = 'nyambucindy0@gmail.com'
    MAIL_PASSWORD = 'rem1436tuit10'
    # SENDER_EMAIL = 'nyambucindy0@gmail.com'


    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/pitches_test'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/pitches_test'    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/pitches'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}