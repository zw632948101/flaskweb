#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_

from datetime import datetime
from flask import render_template, session, redirect, url_for

from app.email import send_email
from . import main
from .forms import NameForm, submitForm
from .. import db
from ..models import User
from ..generate.generate_random_parameter import generateRandomParameter as generate

__author__ = 'wei.zhang'


@main.route('/user/<name>')
def hello_world(name):
    return render_template('user.html', name=name)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['Known'] = False
            if main.config['FLASKY_ADMIN']:
                send_email(main.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', name=user)
        else:
            session['Known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))

    return render_template("index.html", form=form, name=session.get('name'),
                           current_time=datetime.utcnow(), known=session.get('Known', False))


@main.route('/idcard', methods=['GET', 'POST'])
def generate_idcard():
    idcard_submit = submitForm()
    if idcard_submit.validate_on_submit():
        session['idcard'] = generate().generateIdCard()
    return render_template('idcard.html', idcard_submit=idcard_submit, idcard=session.get('idcard'))


@main.route('/redirection')
def redirection():
    return redirect('http://www.baidu.com')
