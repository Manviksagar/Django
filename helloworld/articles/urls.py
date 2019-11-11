from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [

    path('',views.article_list,name='article_list'),
    path('add',views.add, name='add')
]