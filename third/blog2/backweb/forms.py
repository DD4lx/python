from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    # 定义用户名字段
    username = forms.CharField(max_length=10, min_length=4, required=True,
                               error_messages={'required': '用户名不能为空', 'max_length': '用户名长度不能超过10位',
                                               'min_length': '用户名长度不能少于4位'
                                               })

    # 定义密码字段
    userpwd = forms.CharField(max_length=18, required=True,
                              error_messages={
                                  'required': '密码不能为空', 'max_length': '密码长度不能超过18位'
                              })

    # 定义确认密码字段
    userpwd2 = forms.CharField(max_length=18, required=True,
                               error_messages={
                                   'required': '确认密码不能为空', 'max_length': '密码长度不能超过18位'
                               })

    # 定义表单校验方法
    def clean(self):
        # 获取页面中的name值
        name = self.cleaned_data.get('username')
        # 校验用户名是否被注册
        user = User.objects.filter(username=name).first()
        if user:
            # 如果查询已经有该用户名了，返回验证错误信息
            raise forms.ValidationError({'username': '该用户名已经被注册'})
        # 验证密码是否一致
        if self.cleaned_data.get('userpwd2') != self.cleaned_data.get('userpwd'):
            # 不一致就抛出错误信息
            raise forms.ValidationError({'userpwd2': '两次输入密码不一致'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    # 定义登录页面的用户名字段
    username = forms.CharField(max_length=10, min_length=4, required=True,
                               error_messages={'required': '用户名不能为空', 'max_length': '用户名长度不能超过10位',
                                               'min_length': '用户名长度不能少于4位'
                                               })

    # 定义登录页面的用户密码
    userpwd = forms.CharField(max_length=18, required=True,
                              error_messages={
                                  'required': '密码不能为空', 'max_length': '密码长度不能超过18位'
                              })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username': '没有该用户名'})
        return self.cleaned_data
