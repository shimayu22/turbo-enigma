from django import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import tweepy, ssl
ssl._create_default_https_context = ssl._create_unverified_context

def index(self):
    template = loader.get_template("tweet_example/index.html")
    return HttpResponse(template.render())

def tweet_myaccount(self):
    auth = tweepy.OAuthHandler(getenv('API_KEY'), getenv('API_SECRET_KEY'))
    auth.set_access_token(getenv('ACCESS_TOKEN'), getenv('ACCESS_TOKEN_SECRET'))
    api = tweepy.API(auth)
    api.update_status("これはテスト投稿です。tweepyを利用して投稿しています。")

    # Twitterにリダイレクトする
    return redirect('https://twitter.com/home')

def tweet(self):
    # 認証準備
    auth = tweepy.OAuthHandler(getenv('API_KEY'), getenv('API_SECRET_KEY'))

    # Twitter認証画面URLを取得する
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepyException:
        print("Error! Failed to get request token.")

    # ここで認証ページに遷移する
    return redirect(redirect_url)

def callback(request):
    # 認証画面でキャンセルした時の戻り先
    if 'denied' in request.GET.dict():
        return redirect(getenv('BACK_URL'))
    
    # 認証した場合の処理
    # ツイートするユーザーのトークンを取得する準備
    auth = tweepy.OAuthHandler(getenv('API_KEY'), getenv('API_SECRET_KEY'))
    auth.request_token['oauth_token'] = oauth_token = request.GET['oauth_token']
    auth.request_token['oauth_token_secret'] = oauth_verifier = request.GET['oauth_verifier']

    # ツイートするユーザーのシークレットトークンを取得する
    try:
        auth.get_access_token(oauth_verifier)
    except tweepy.TweepyException:
        print("Error! Failed to get request token.")
    
    # ツイートする
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)
    api.update_status("認証画面を経由して投稿しています。テスト投稿です。")

    # Twitterにリダイレクトする
    return redirect('https://twitter.com/home')
