# coding=utf-8


from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, HttpResponseRedirect 
from django.shortcuts import redirect


class Mids(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        ''' 调用视图前识别是手机端，还是pc端 '''
        MOBILE_USER_AGENTS = ['Android', 'iPhone']
        current_user_agent = request.META['HTTP_USER_AGENT']
        print '------------------------'
        # return HttpResponseRedirect('/indexs/index')

        # for ua in MOBILE_USER_AGENTS:        
        #     if ua in current_user_agent:
        #         return HttpResponseRedirect(reverse('/indexs/mobileIndex/'))
        # else:
        #         return HttpResponseRedirect('/indexs/index/')
