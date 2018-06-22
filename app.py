import os

from flask import Flask, request, make_response, redirect, abort, render_template, session, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from generate_random_parameter import generateRandomParameter as generate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class submitForm(FlaskForm):
    submit = SubmitField('提交')


class NameForm(Form):
    name = StringField('你的名字是?', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/user/<name>')
def hello_world(name):
    return render_template('user.html', name=name)


@app.route('/', methods=['GET', 'POST'])
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('您更新了名字 !')
        session['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'),
                           current_time=datetime.utcnow())


@app.route('/idcard', methods=['GET', 'POST'])
def generate_idcard():
    idcard_submit = submitForm()
    if idcard_submit.validate_on_submit():
        session['idcard'] = generate().generateIdCard()
    return render_template('idcard.html', idcard_submit=idcard_submit, idcard=session.get('idcard'))


@app.route('/redirection')
def redirection():
    return redirect('http://www.baidu.com')


@app.errorhandler(404)
def page_not_page(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
