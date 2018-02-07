#coding:utf-8
from django.db import models

class Server(models.Model):
    #python orm id默认有
    #python orm 字段默认不为空
    system = models.CharField(max_length = 32,verbose_name = "系统类型")
    ip = models.CharField(max_length = 32)
    mac = models.CharField(max_length = 32)
    controler = models.CharField(max_length = 32,verbose_name = "管理员")
    statue = models.CharField(max_length = 8,verbose_name = "状态")

# Create your models here.
