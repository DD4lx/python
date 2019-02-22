import datetime
import random

from django.http import HttpResponseRedirect
from django.urls import reverse


def login_required(func):
    def check_login(request):
        try:
            request.session['user_id']
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)
    return check_login

def get_order_sn():
    """
    生成随机的订单号
    """
    sn = ''
    s='1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(10):
        sn += random.choice(s)
    sn += datetime.now().strftime('%Y%m%d%H%M%S')
    return sn