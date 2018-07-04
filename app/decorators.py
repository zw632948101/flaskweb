#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permissions

__author__ = 'wei.zhang'


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_reuired(f):
    return permission_required(Permissions.ADMINISTER)(f)
