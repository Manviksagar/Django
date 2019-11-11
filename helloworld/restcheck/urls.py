from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [


    url('employee',views.emplist.as_view())
]