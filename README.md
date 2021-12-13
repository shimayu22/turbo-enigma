# これなに？
[Django Advent Calendar 2021](https://qiita.com/advent-calendar/2021/django)の16日目の記事用サンプルです。

Twitter APIを利用してツイートします。

# # 環境

- Python 3.8.1
- Django 4.0

# 初期設定

ひとまずvenvで動きます。

### Win版
    python -m venv env
    env\Sctipts\activate
    pip install -r requirements.txt
    type nul > local_settings.py
    python config/get_random_secret_key.py >> config/local_settings.py
    manage.py migrate
    manage.py createsuperuser
    manage.py runserver

### Mac版
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    touch config/local_settings.py
    python config/get_random_secret_key.py >> config/local_settings.py
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    