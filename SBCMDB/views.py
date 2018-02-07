#coding:utf-8

from django.shortcuts import render,render_to_response

def index(request):
    return render_to_response("index.html",locals())

def server_list(request):
    return render_to_response("server_list.html",locals())