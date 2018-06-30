#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from app import db
from app.models import User
from . import auth
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LonginForm, RegistrationForm, ChangePasswordForm
from ..eamil import send_email

__author__ = 'wei.zhang'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """登录"""
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
    """注销账户"""
    logout_user()
    flash("你已注销.")
    return redirect(url_for('main.index'))


@auth.route('/secret')
@login_required
def secret():
    return "只能登录用户访问"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """注册账户,并发送激活邮件"""
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        # send_email(user.email, '确认你的账户.', 'auth/email/confirm', user=user, token=token)
        send_email('632948101@qq.com', '确认你的账户.', 'auth/email/confirm', user=user, token=token)
        flash("注册成功,请到邮箱中确认你的账户")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    """激活账户"""
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash("你的账户已激活成功.可以进行登录")
    else:
        flash("激活链接无效或已过期,请重新生成")
    return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
    """使用钩子,判断登录用户是否激活"""
    if current_user.is_authenticated:
        if not current_user.confirmed and request.endpoint[:5] != 'auth.' and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    """判断用户是否登录,如果没有登录显示重新发送邮件页面"""
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirmed')
@login_required
def login_confirmation():
    """重发激活邮件"""
    token = current_user.generate_confirmation_token()
    # send_email(current_user.email, "重新发送确认邮件", 'auth/email/confirm', user=current_user, token=token)
    send_email('632948101@qq.com', "重新发送确认邮件", 'auth/email/confirm', user=current_user, token=token)
    flash("已重新发送确认邮件至注册邮箱")
    return redirect(url_for('main.index'))


@auth.route('/change_password', methods=['POST', 'GET'])
@login_required
def change_password():
    """修改密码"""
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            if form.old_password.data != form.new_password.data:
                current_user.password = form.new_password.data
                db.session.add(current_user)
                db.session.commit()
                flash("修改密码成功")
                return redirect(url_for("main.index"))
            else:
                flash("新密码不能与旧密码相同.")
        else:
            flash("旧密码错误,请输入正确的旧密码")
    return render_template("auth/reset_password.html", form=form)

# def password_reset_request():
