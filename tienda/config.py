from decouple import config

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'tienda'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587  # TLS: Transport Layer Security: Seguridad de la capa de transporte
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'correo@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
