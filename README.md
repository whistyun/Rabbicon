# Rabbicon

## 概要

(今のところ)Flaskの勉強用に作成

## 実行方法

下記コマンドで実行可能

```cmd
python testrun.py
```

現状、4つのURLを用意してます。
|URL|説明|
|----------|----------|
| http://localhost:5000/      | (ログイン不要)稼働確認用ページ |
| http://localhost:5000/login | ログイン用ページ |
| http://localhost:5000/index | (ログイン要)ログイン後のページ。ログインしていない状態で、アクセスした場合はloginに遷移させられる。 |
| http://localhost:5000/login | ログアウト用ページ |

なお、ユーザー/パスワード は伝統ある root/password です。

## フォルダ構成

```
/
├─rabbicon/       コントローラー関係のpythonスクリプト配置用
│
├─static/         静的なファイル配置用
│
└─templates/      テンプレートファイル(jinja2)配置用
```