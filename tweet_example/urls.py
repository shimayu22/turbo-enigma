from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet', views.tweet, name='tweet'),
    path('callback', views.callback, name='callback'),
]