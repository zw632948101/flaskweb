#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, abort, flash
from flask_login import current_user, login_required

from app.eamil import send_email
from ..main.forms import NameForm, submitForm, EditProfileForm
from . import main
from .. import db
from ..models import User
from ..generate.generate_random_parameter import generateRandomParameter as generate

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
