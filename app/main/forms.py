#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

__author__ = 'wei.zhang'


class submitForm(FlaskForm):
    submit = SubmitField('提交')


class NameForm(FlaskForm):
    name = StringField('你的名字是?', validators=[DataRequired()])
    submit = SubmitField('提交')
