import os

from flask import Flask
import flask_login

import rabbicon

# Flaskの初期化
app = Flask(__name__)
app.secret_key = os.urandom(32)

# Flask-Loginのセットアップ
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

def start(host=None, port=5000, debug=False):

    # 読み込みしたいモジュールを初期化
    # TODO フォルダごとにURLの階層を分ける場合は、Blueprintを使用する？
    # @see http://flask.pocoo.org/docs/0.12/blueprints/
    rabbicon.init()

    # start

    if host:
        app.run(host=host, port=port, debug=debug)

    else:
        app.run(port=port, debug=debug)
