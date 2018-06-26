#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email

__author__ = 'wei.zhang'


class LonginForm(FlaskForm):
    email = StringField('邮箱 :', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码 :', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')
