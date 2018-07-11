#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from datetime import datetime
from flask import render_template, session, redirect, url_for, abort, flash
from flask_login import current_user, login_required
from ..main.forms import submitForm, EditProfileForm, EditProfileAdminForm
from . import main
from .. import db
from ..models import User, Role
from ..generate.generate_random_parameter import generateRandomParameter as generate
from ..decorators import admin_required

__author__ = 'wei.zhang'


@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/idcard', methods=['GET', 'POST'])
def generate_idcard():
    idcard_submit = submitForm()
    if idcard_submit.validate_on_submit():
        session['idcard'] = generate().generateIdCard()
    return render_template('idcard.html', idcard_submit=idcard_submit, idcard=session.get('idcard'))


@main.route('/redirection')
def redirection():
    return redirect('http://www.baidu.com')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@main.route('/edit_profile', methods=['POST', 'GET'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('你的用户资料已更新.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit_profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('已对这个用户更新')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)
