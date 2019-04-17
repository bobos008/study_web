# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import ClassicCase, CorporateNews, CompanyInfo, FriendlyUrl 

# Create your views here.
def index(request):
    return render(request, 'indexs/index.html')


def advantage(request):
    return render(request, 'indexs/advantage.html')


def brandHistory(request):
    return render(request, 'indexs/brand-history.html')


def classicCase(request):
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
        'allow_click': allow_click}
    return render(request, 'indexs/classic-case.html', cases_data)


def corporateNews(request):
    corporate_news_set = CorporateNews.objects.values(
        'news_title',
        'thumb_img',
        'news_push_date',
        'news_description',
    ).order_by('-news_id')
    # news_num = len(corporate_news_set)
    company_info = CompanyInfo.objects.get(pk=1)
    # print '------------------------'
    # print company_info
    news_data = {
        'news_set': corporate_news_set,
        'company_info': company_info
    }
    return render(request, 'indexs/corporate-news.html', news_data)


'''
手机端
'''
def mobileIndex(request):
    return render(request, 'mobile/mobileindex.html')
