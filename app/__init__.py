#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
<<<<<<< HEAD

=======
>>>>>>> exercise_email_porject_20180623_zhangwei
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
<<<<<<< HEAD

__author__ = 'wei.zhang'

=======
from flask_login import LoginManager

__author__ = 'wei.zhang'

"""创建构造文件,导入正在使用的flask扩展"""

>>>>>>> exercise_email_porject_20180623_zhangwei
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
<<<<<<< HEAD
=======
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
>>>>>>> exercise_email_porject_20180623_zhangwei


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
<<<<<<< HEAD

=======
>>>>>>> exercise_email_porject_20180623_zhangwei
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
<<<<<<< HEAD
=======
    login_manager.init_app(app)
    # 附加路由和自定义的错误页面
>>>>>>> exercise_email_porject_20180623_zhangwei

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

<<<<<<< HEAD
=======
    from .auth import auth as auth_bluepring
    app.register_blueprint(auth_bluepring, url_prefix='/auth')

>>>>>>> exercise_email_porject_20180623_zhangwei
    return app
