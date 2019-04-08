# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'indexs/index.html')


def advantage(request):
    return render(request, 'indexs/advantage.html')


def brandHistory(request):
    return render(request, 'indexs/brand-history.html')


def classicCase(request):
    return render(request, 'indexs/classic-case.html')


def corporateNews(request):
    return render(request, 'indexs/corporate-news.html')
