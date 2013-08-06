#-*-coding: utf8-*-
from django import forms
from django.contrib.auth.models import User

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=200, label="")

class UserRegistForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='用户名', error_messages={'required': '用户名不能为空！'})
    password = forms.CharField(label='密码', error_messages={'required': '密码不能为空'})
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = { 
            'password': forms.PasswordInput()
        }   

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='用户名', error_messages={'required': '用户名不能为空！'})
    password = forms.CharField(widget=forms.PasswordInput, label='密码', error_messages={'required': '密码不能为空'})





