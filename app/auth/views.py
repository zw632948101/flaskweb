#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from flask import render_template
from . import auth

__author__ = 'wei.zhang'


@auth.route('/login')
def login():
    return render_template('auth/login.html')
