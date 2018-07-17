#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from app.models import Role, User

__author__ = 'wei.zhang'

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError


class submitForm(FlaskForm):
    submit = SubmitField('提交')


class NameForm(FlaskForm):
    name = StringField('你的名字是?', validators=[DataRequired()])
    submit = SubmitField('提交')


class EditProfileForm(FlaskForm):
    name = StringField('真实姓名:', validators=[Length(0, 64)])
    location = StringField("联系地址:", validators=[Length(0, 64)])
    about_me = TextAreaField("自诉 : ")
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField("邮箱 : ", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField("昵称:", validators=[DataRequired(), Length(1, 64),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '昵称必须是字母数字和_.')])
    confirmed = BooleanField("Confirmed")
    role = SelectField('权限', coerce=int)
    name = StringField('真实姓名:', validators=[Length(0, 64)])
    location = StringField('联系地址:', validators=[Length(0, 64)])
    about_me = TextAreaField('自诉 : ')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已注册,请更换邮箱后重试.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已使用,请更换后重试.')


class PostForm(FlaskForm):
    body = TextAreaField('发表你的看法', validators=[DataRequired()])
    submit = SubmitField('提交文章')
