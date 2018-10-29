from django.http import HttpResponseRedirect
from django.urls import reverse

from user.models import UserToken


def login_required(func):

    def check_login(request):
        # func 是被login_required装饰的函数
        # 获取浏览器中的COOKIES的值
        token = request.COOKIES.get('token')
        # 如果没有cookie,说明用户没登录过或者cookie被删除了
        if not token:
            return HttpResponseRedirect(reverse('user:login'))
        # 查询数据库中的标识符的值
        # 在数据库中查询是否有用户的cookie令牌是浏览器中的令牌
        user_token = UserToken.objects.filter(token=token).first()
        # 如果没有，就说明用户标识符有错，重新登录
        if not user_token:
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)
    return check_login
