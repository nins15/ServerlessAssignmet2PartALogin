from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import mysql.connector

db = mysql.connector.connect(host="127.0.0.1", user="root", password="Hanumann@1",
                             auth_plugin='mysql_native_password',database='testdatabase')
from os import  path
#database_name="database.db"
def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']='ninad'


    #  app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{database_name}'
 #   db.init_app(app)
    from .views import views
    from .Login import Login
    # bcrypt = Bcrypt(app=app)

    app.register_blueprint(Login, url_prefix='/')
    app.register_blueprint(views,url_prefix='/')
    #app.register_blueprint(Login, url_prefix='/')

    #from .model import User,LoginInfo
#    create_database(app)
    return app
# def create_database(app):
#     if not path.exists('website/'+database_name):
#         db.create_all(app=app)
#         print('Created Database')
