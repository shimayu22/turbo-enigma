from django import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import tweepy

def index(self, request):
    template = loader.get_template("tweet_example/index.html")
    return HttpResponse(template.render())

def tweet_myaccount(self, request):

    # ここで認証ページに遷移する
    return redirect(redirect_url)

def tweet(self, request):

     # Twitter認証画面URLを取得する
    auth = tweepy.OAuthHandler(getenv('CONSUMER_KEY'), getenv('CONSUMER_SECRET'))


    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepyException:
        print("Error! Failed to get request token.")

    # ここで認証ページに遷移する
    return redirect(redirect_url)

def callback(self, request):
    # 認証画面でキャンセルした時の戻り先
    if 'denied' in request.query_params.dict():
        return redirect(getenv('BACK_URL'))
    
    # 認証した場合の処理
    # ツイートするユーザーのトークンを取得する準備
    auth = tweepy.OAuthHandler(getenv('CONSUMER_KEY'), getenv('CONSUMER_SECRET'))
    auth.request_token['oauth_token'] = oauth_token = request.query_params['oauth_token']
    auth.request_token['oauth_token_secret'] = oauth_verifier = request.query_params['oauth_verifier']

    # ツイートするユーザーのシークレットトークンを取得する
    try:
        auth.get_access_token(oauth_verifier)
    except tweepy.TweepyException:
        print("Error! Failed to get request token.")
    
    # ツイートする
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)
    api.update_status("これはテスト投稿です。tweepyを使って投稿しています。")

    # Twitterにリダイレクトする
    return redirect('https://twitter.com/home')
