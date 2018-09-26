# -*- coding: utf-8 -*-

from flask import redirect, render_template, request, url_for
import flask_login

from application import app, login_manager

@app.route('/')
def hellow():
    return 'rabbicon is work!'

@app.route('/index')
@flask_login.login_required
def index():
    return 'welcome'