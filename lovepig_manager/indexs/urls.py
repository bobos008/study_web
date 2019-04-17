# coding=utf-8


from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^advantage/', views.advantage),
    url(r'^brandHistory/', views.brandHistory),
    url(r'^classicCase/', views.classicCase),
    url(r'^corporateNews/', views.corporateNews),
    url(r'^mobileIndex/', views.mobileIndex),
]
