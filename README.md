# これなに？
[Django Advent Calendar 2021](https://qiita.com/advent-calendar/2021/django)の16日目の記事用サンプルです。

Twitter APIを利用してツイートします。

# 環境

- Python 3.8.1
- Django 4.0

# 初期設定

ひとまずvenvで動きます。

## Win版
    python -m venv env
    env\Sctipts\activate
    pip install -r requirements.txt
    type nul > local_settings.py
    python config/get_random_secret_key.py >> config/local_settings.py
    type nul > .env


## Mac版
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    touch config/local_settings.py
    python config/get_random_secret_key.py >> config/local_settings.py
    touch .env

## .envファイルにキーを入力する
- [Twitterデベロッパーサイト](https://developer.twitter.com/en/portal/dashboard)でアプリを申請した時に取得した各種キーを.envファイルに記入します
- （例）

```
API_KEY=xxxxxxxxxxxxxxxxxxx
API_SECRET_KEY=xxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxx
```

## CallbackURLを設定する
- [Twitterデベロッパーサイト](https://developer.twitter.com/en/portal/dashboard)の`CALLBACK URLS`のURLを`http://127.0.0.1:8000/`に設定する
  - ここでは`python manage.py runserver`で使用されるURLを指定しています

## サーバーを起動する
- `python manage.py runserver`

# ボタンをクリックするとツイートする
## 自分のアカウントでツイートする
- 「ボタンを押すと自分のアカウントでツイートします」の下のボタンを押すとログインしている自分のアカウントでツイートします。

## 認証画面経由でツイートする
- 「ボタンを押すと認証画面経由でツイートします」の下のボタンを押すと、認証画面経由でツイートします。
