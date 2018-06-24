#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_required, login_user, logout_user
from ..models import User
from .forms import LoginForm

__author__ = 'wei.zhang'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("无效的用户名和密码.")
    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("您已退出登录")
    return redirect(url_for("main.index"))


@auth.route('/secret')
@login_required
def secret():
    return "只允许登录用户访问,请登录后访问!"
