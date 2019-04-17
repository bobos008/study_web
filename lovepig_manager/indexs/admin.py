# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ClassicCase, CorporateNews, CompanyInfo, FriendlyUrl

# Register your models here.
@admin.register(ClassicCase)
class ClassicCaseAdmin(admin.ModelAdmin):
    search_fields = ['case_title', 'house_style', 'houting_date', 'client_name']
    list_display = ['small_title', 'case_title', 'client_name', 'hosting_date', 'case_content', 'house_style']


@admin.register(CorporateNews)
class CorporateNewsAdmin(admin.ModelAdmin):
    search_fields = ['news_title', 'news_push_date']
    list_display = ['news_title', 'news_push_date', 'news_description']
    list_per_page = 10


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'company_name', 'company_email', 'landline', 'case_number', 'bussness_num']
    # fields = ('company_id', 'company_name', 'company_email', 'landline', 'case_number', 'bussness_num')


@admin.register(FriendlyUrl)
class FriendlyUrlAdmin(admin.ModelAdmin):
    search_fields = ['url_name', 'urls']
    list_display = ['url_name', 'urls']
    empty_value_display = '---empty---'
