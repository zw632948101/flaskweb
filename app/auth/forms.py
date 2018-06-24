#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, DataRequired

__author__ = 'wei.zhang'


class LoginForm(FlaskForm):
    email = StringField('邮箱 : ', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("密码 : ", validators=[DataRequired()])
    remember_me = BooleanField("记住登录")
    submit = SubmitField('登录')
