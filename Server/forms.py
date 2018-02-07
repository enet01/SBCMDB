#coding:utf-8
from django import forms
from models import Server

class OurForm(forms.Form):
    system = forms.CharField(max_length=32, label="系统类型")
    ip = forms.CharField(max_length=32)
    mac = forms.CharField(max_length=32)
    controler = forms.CharField(max_length=32, label="管理员")
    statue = forms.CharField(max_length=8, label="状态")

class ServerForm(forms.ModelForm):
    class Meta:
        model=Server
        fields=("system","ip","mac","controler","statue")
