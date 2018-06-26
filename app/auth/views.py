#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from app.models import User
from . import auth
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user
from .forms import LonginForm

__author__ = 'wei.zhang'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LonginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效的用户名和密码')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("你已注销.")
    return redirect(url_for('main.index'))


@auth.route('/secret')
@login_required
def secret():
    return "只能登录用户访问"
