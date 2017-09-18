from django.conf.urls import url
from django.contrib import admin

from .views import Hello,TestHello

urlpatterns = [

    url(r'^test/', TestHello, name='TestHello'),
    url(r'^$', Hello, name='Hello')
]
