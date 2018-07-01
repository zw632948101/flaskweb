#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from . import main
from flask import render_template
__author__ = 'wei.zhang'

@main.app_errorhandler(404)
def page_not_page(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
