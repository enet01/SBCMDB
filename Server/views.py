#coding:utf-8
from models import Server
from django.shortcuts import render_to_response,render
from forms import *

def serverlist(request):
    all_service = Server.objects.all()
    #all_s = Server.objects.raw("select * from server_server")
    return render_to_response("server_list.html",locals())


def register(request):
    regist=ServerForm()
    return render_to_response("server_register.html", local())


def service(request,id):
    return render_to_response("service.html",locals())



# Create your views here.
