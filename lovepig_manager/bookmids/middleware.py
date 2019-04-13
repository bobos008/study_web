# coding=utf-8


from django.http import HttpResponseRedirect 
from django.utils.deprecation import MiddlewareMixin


class Mids(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        ''' 调用视图前识别是手机端，还是pc端 '''
        MOBILE_USER_AGENTS = ['Android', 'iPhone']
        current_user_agent = request.META['HTTP_USER_AGENT']

        current_url = request.path
        if current_url != '/indexs/mobileIndex/':
            for ua in MOBILE_USER_AGENTS:        
                if ua in current_user_agent:
                    return HttpResponseRedirect('/indexs/mobileIndex/')
        else:
            return 
