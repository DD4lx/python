from django import forms

from user.models import User


# 注册表单
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=18, required=True,
                                error_messages={'max_length': '用户名最长为18个字符',
                                                'required': '用户名必填'})
    pwd = forms.CharField(max_length=20, required=True,
                          error_messages={'max_length': '密码最长为20个字符',
                                          'required': '密码必填'})
    cpwd = forms.CharField(max_length=20, required=True,
                           error_messages={'max_length': '密码最长为20个字符',
                                           'required': '确认密码必填'})
    email = forms.CharField(max_length=50, required=True,
                            error_messages={'max_length': '邮箱最长为50个字符',
                                            'required': '邮箱地址必填'})

    def clean(self):
        # 获取用户名，用于校验用户是否已经注册
        user_name = self.cleaned_data.get('user_name')
        # 校验用户是否注册
        user = User.objects.filter(username=user_name)
        if user:
            raise forms.ValidationError({'user_name': '该用户名已被注册'})
        # 校验密码是否输出正确
        if self.cleaned_data.get('pwd') != self.cleaned_data.get('cpwd'):
            raise forms.ValidationError({'pwd': '两次密码输入不一致'})
        return self.cleaned_data


# 登录表单
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=18, required=True,
                               error_messages={'max_length': '用户名最长为18位',
                                               'required': '用户名必填'})
    pwd = forms.CharField(max_length=20, required=True,
                          error_messages={'max_length': '密码最长为20位',
                                          'required': '密码必填'})

    def clean(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError({'username': '没有该用户'})
        return self.cleaned_data


# 用户地址表单
class UserAddressForm(forms.Form):
    # 用户地址保存的表单验证
    signer_name = forms.CharField(required=True, error_messages={'required': '收件人必填'})
    address = forms.CharField(required=True, error_messages={'required': '详细地址必填'})
    signer_mobile = forms.CharField(required=True, error_messages={'required': '收件人手机号码必填'})
    signer_postcode = forms.CharField(required=True, error_messages={'required': '邮编必填'})