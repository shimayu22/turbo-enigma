from django import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import tweepy

def index(request):
    template = loader.get_template("tweet_example/index.html")
    return HttpResponse(template.render())

def tweet(request):
    return redirect()

def callback(request):
    return redirect()
