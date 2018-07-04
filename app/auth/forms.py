#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from ..models import User

__author__ = 'wei.zhang'


class LonginForm(FlaskForm):
    """登录表单"""
    email = StringField('邮箱 :', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码 :', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    """注册账户表单"""
    email = StringField('邮箱 : ', validators=[DataRequired(), Length(1, 64, message="邮箱格式错误,请重新姿态那些."), Email()])
    username = StringField('昵称 : ', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                      '昵称必须只能是字母,数字,下划线和点')])
    password = PasswordField('密码 : ', validators=[DataRequired(), EqualTo('password2', message='密码不一致'),
                                                  Regexp('^[A-Z][A-Za-z0-9_.]*$', 0, "密码必须以大写字母开头")])
    password2 = PasswordField('确认密码:', validators=[DataRequired()])
    submit = SubmitField("注册")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已被注册')


class ChangePasswordForm(FlaskForm):
    """修改密码表单"""
    old_password = PasswordField("原密码 :", validators=[DataRequired()])
    new_password = PasswordField("新密码 :", validators=[DataRequired(), EqualTo("new_password2", message="两次密码不一致"),
                                                      Regexp('^[A-Z][A-Za-z0-9_.]*$', 0, "密码必须以大写字母开头")])
    new_password2 = PasswordField("确认密码:", validators=[DataRequired()])
    submit = SubmitField("修改密码")



class PasswordResetForm(FlaskForm):
    password = PasswordField('新密码 :', validators=[DataRequired(), EqualTo("password2", message="两次密码不一致"),
                                                  Regexp('^[A-Z][A-Za-z0-9_.]*$', 0, "密码必须以大写字母开头")])
    password2 = PasswordField('确认密码:', validators=[DataRequired()])
    submit = SubmitField("重置密码")


class PasswordResetRequestForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField("重置密码")


class ChangeEmailReauestForm(FlaskForm):
    email = StringField("新邮箱:", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码:', validators=[DataRequired()])
    submit = SubmitField("修改邮箱")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')


class ChangeUsernameForm(FlaskForm):
    username = StringField('昵称 : ', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                      '昵称必须只能是字母,数字,下划线和点')])
    submit = SubmitField("修改昵称")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已被注册')
