#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from app import db
from app.models import User
from . import auth
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LonginForm, RegistrationForm, ChangePasswordForm, PasswordResetForm, PasswordResetRequestForm, \
    ChangeEmailReauestForm, ChangeUsernameForm
from ..eamil import send_email

__author__ = 'wei.zhang'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """登录"""
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
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
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))
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
    return render_template("auth/change_password.html", form=form)


@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    """发送重置密码邮件"""
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_confirmation_token()
            # send_email(user.email, '重置密码', 'auth/email/reset_password', user=user, token=token)
            send_email("632948101@qq.com", '重置密码', 'auth/email/reset_password', user=user, token=token)
            flash("已发送重置密码邮件,请到邮箱中查看")
            return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """设置重置密码"""
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        if User.reset_password(token, form.password.data):
            if User.reset_pasword_verify(token, form.password.data):
                db.session.commit()
                flash("密码重置成功")
                return redirect(url_for('auth.login'))
            else:
                flash("新密码不能与旧密码相同.")
        else:
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('change_email', methods=['GET', 'POST'])
def change_email_request():
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))
    form = ChangeEmailReauestForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = current_user.generate_email_change_toekn(new_email)
            # send_email(new_email, "修改邮箱", 'auth/email/change_email', user=current_user, token=token)
            send_email("632948101@qq.com", "修改邮箱", 'auth/email/change_email', user=current_user, token=token)
            flash("修改邮箱激活邮件已发送到你新邮箱,请查收")
            return redirect(url_for('main.index'))
        else:
            flash("无效的邮箱或密码")
    return render_template('auth/change_email.html', form=form)


@auth.route('change_email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        db.session.commit()
        flash("你的电子邮箱已更新")
    else:
        flash("无效的请求")
    return redirect(url_for('main.index'))


@auth.route('/change_username', methods=['GET', 'POST'])
@login_required
def change_username():
    """修改昵称"""
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))
    form = ChangeUsernameForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.add(current_user)
        db.session.commit()
        flash("修改昵称成功")
        return redirect(url_for('main.index'))
    return render_template('auth/change_username.html', form=form)
