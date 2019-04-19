# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import ClassicCase, CorporateNews, CompanyInfo, FriendlyUrl 

# Create your views here.
def index(request):
    choose_menu = '1'
    datas = {
        'choose_menu': choose_menu
    }
    return render(request, 'indexs/index.html', datas)


def advantage(request):
    choose_menu = '2'
    datas = {
        'choose_menu': choose_menu
    }
    return render(request, 'indexs/advantage.html', datas)


def brandHistory(request):
    choose_menu = '4'
    datas = {
        'choose_menu': choose_menu
    }
    return render(request, 'indexs/brand-history.html', datas)


def classicCase(request):
    choose_menu = '3'
    classic_case_set = ClassicCase.objects.values(
        'small_title',
        'case_title',
        'cover',
        'client_name',
        'hosting_date',
        'house_style').order_by('-case_id')
    cases_num = len(classic_case_set)
    allow_click = True
    # 限制显示个数
    if cases_num > 4:
        classic_case_set = classic_case_set[:4]
    if (cases_num < 3) and (cases_num > 0):
        allow_click = False
    cases_data = {
        'classic_case_set': classic_case_set,
        'allow_click': allow_click,
        'choose_menu': choose_menu
        }
    return render(request, 'indexs/classic-case.html', cases_data)


def corporateNews(request):
    choose_menu = '5'
    corporate_news_set = CorporateNews.objects.values(
        'news_title',
        'thumb_img',
        'news_push_date',
        'news_description',
    ).order_by('-news_id')[:4]
    # news_num = len(corporate_news_set)
    company_info = CompanyInfo.objects.get(pk=1)
    news_data = {
        'news_set': corporate_news_set,
        'company_info': company_info,
        'choose_menu': choose_menu
    }
    return render(request, 'indexs/corporate-news.html', news_data)


'''
手机端
'''
def mobileIndex(request):
    corporate_news_set = CorporateNews.objects.values(
        'news_title',
        'thumb_img',
        'news_push_date',
        'news_description'
    ).order_by('-news_id')[:4]
    company_info = CompanyInfo.objects.get(pk=1)
    classic_case_set = ClassicCase.objects.values(
        'small_title',
        'case_title',
        'cover',
        'client_name',
        'hosting_date',
        'house_style').order_by('-case_id')
    cases_num = len(classic_case_set)
    # 限制显示个数
    if cases_num > 4:
        classic_case_set = classic_case_set[:4]
    datas = {
        'compnay_info': company_info,
        'news_set': corporate_news_set,
        'classic_case_set': classic_case_set
    }
    return render(request, 'mobile/mobileindex.html', datas)
