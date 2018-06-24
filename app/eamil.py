#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'
from flask import render_template
from . import mail, create_app
from threading import Thread
from flask_mail import Message


def send_email(to, subject, templte, **kwargs):
    app = create_app().__getattribute__()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(templte + '.txt', **kwargs)
    msg.html = render_template(templte + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
