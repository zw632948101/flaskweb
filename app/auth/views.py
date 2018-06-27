#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from app import db
from app.models import User
from . import auth
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LonginForm, RegistrationForm
from ..eamil import send_email
from app import create_app

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


@auth.route('/register', methods=['GET', 'POST'])
def register():
    app = current_user._get_current_object()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(app.config['FLASKY_ADMIN'], '确认你的账户.', 'auth/email/confirm', user=user, token=token)
        flash("注册成功,请到邮箱中确认你的账户")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirmed(token):
        flash("你的账户已激活成功.可以进行登录")
    else:
        flash("激活链接无效或已过期,请重新生成")
    return redirect(url_for('main.index'))
