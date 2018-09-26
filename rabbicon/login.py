# -*- coding: utf-8 -*-

from flask import redirect, render_template, request, url_for
import flask_login

from application import app, login_manager


class User(flask_login.UserMixin):
    pass


# TODO 何のために必要か確認 @see https://github.com/maxcountryman/flask-login
@login_manager.user_loader
def user_load(userid):
    app.logger.info('call user_load')

    user    = User()
    user.id = userid
    return user


# TODO 何のために必要か確認 @see https://github.com/maxcountryman/flask-login
@login_manager.request_loader
def request_loader(request):
    app.logger.info('call request loader')

    __authenticate_user(request)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("login.html", status = 'NG', message = 'ログインが必要です')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    app.logger.info('call login')

    # GETならログインページへ
    if request.method == 'GET':
        return render_template("login.html", status = 'OK', message = None)    

    # 未入力チェック
    if request.form.get('userid', default='') == '' \
            or request.form.get('passwd', default='') == '':
        return render_template("login.html", status = 'NG', message = '未入力の項目があります')

    # ユーザ検証
    user = __authenticate_user(request)
    if user and flask_login.login_user(user):
        # accepted
        return redirect(url_for('index'))

    else:
        # rejected
        return render_template("login.html", status = 'NG', message = '知らない子ですね')


def __authenticate_user(request):
    userid = request.form.get('userid', default=None)
    passwd = request.form.get('passwd', default=None)

    # 適当な、ユーザ検証
    if userid == 'root' and passwd == 'password':
        app.logger.info('user "%s" accepted', userid)
        user    = User()
        user.id = userid

        return user

    else:
        app.logger.info('user "%s" rejected', userid)
        return None


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Bye!'