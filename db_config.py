class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/link_shortener_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
