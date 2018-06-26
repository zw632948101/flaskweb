#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import forms, views

__author__ = 'wei.zhang'
