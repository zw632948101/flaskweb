#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permissions

__author__ = 'wei.zhang'


@main.app_context_processor
def inject_permissions():
    return dict(Permissions=Permissions)
