#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from ..models import User

__author__ = 'wei.zhang'


class LonginForm(FlaskForm):
    email = StringField('邮箱 :', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码 :', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('邮箱 : ', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('昵称 : ', validators=[DataRequired(), Length(1, 64), Regexp('^[A-za-z][A-Za-z0-9_.]*$', 0,
                                                                                      '昵称必须只能是字母,数字,下划线和点')])
    password = PasswordField('密码 : ', validators=[DataRequired(), EqualTo('password2', message='密码不一致')])
    password2 = PasswordField('确认密码:', validators=[DataRequired()])
    submit = SubmitField("注册")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已被注册')
