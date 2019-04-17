# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class ClassicCase(models.Model):
    ''' 经典案例 '''
    case_id = models.AutoField(primary_key=True)
    small_title = models.CharField(u'小标题', help_text='小标题最多输入4个汉字!', max_length=4)
    case_title = models.CharField(u'大标题', max_length=32, help_text='大标题最多输入32个汉字！')
    client_name = models.CharField(u'托管人', max_length=16, help_text='托管人名字最多输入16个汉字！')
    hosting_date = models.DateField(u'托管时间')
    cover = models.ImageField(u'封面', upload_to='static/imgs/', help_text='注意图片大小:<span style="color:red;">550×346像素</span>')
    case_content = models.TextField(u'民宿概况')
    house_style = models.CharField(u'房屋风格', max_length=32, help_text='房屋风格最多输入16个汉字！')

    class Meta:
        verbose_name_plural = u'经典案例'


class CorporateNews(models.Model):
    ''' 企业新闻 '''
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(u'新闻标题', max_length=21, help_text='新闻标题最多输入21个汉字!')
    thumb_img = models.ImageField(u'缩略图', upload_to="static/imgs/", help_text='注意缩略图大小：<span style="color:red;">207×207像素</span>')
    news_img = models.ImageField(u'详情图片', upload_to="static/imgs/", help_text='注意图片大小：<span style="color:red;">未知</span>')
    news_push_date = models.DateField(u'发表时间') 
    news_description = models.CharField(u'部分描述', max_length=100, default="", help_text='是文章详情前面一部分内容，字数最好在100以内！')
    news_detail = HTMLField(u'详细')
    
    class Meta:
        verbose_name_plural = u'企业新闻'


class CompanyInfo(models.Model):
    ''' 企业信息 '''
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(u'公司名称', max_length=32, help_text='公司名称最多输入32个汉字!')
    company_email = models.EmailField(u'公司邮箱', max_length=120, help_text='公司邮箱最多输入120个字符！')
    landline = models.CharField(u'座机', max_length=32)
    wechat_img = models.ImageField(u'公司二维码', upload_to='static/imgs/', help_text='注意二维码图片大小：<span style="color:red;">120×120像素</span>')
    case_number = models.CharField(u'备案号', max_length=240)
    bussness_num = models.CharField(u'营业执照号', max_length=240)

    class Meta:
        verbose_name_plural = u'企业信息'


class FriendlyUrl(models.Model):
    ''' 友情链接 '''
    friendly_id = models.AutoField(primary_key=True)
    url_name = models.CharField(u'网址名称', max_length=12, help_text='网址名称最多输入12个汉字！')
    urls = models.CharField(u'链接', max_length=800)

    class Meta:
        verbose_name_plural = u'友情链接'
