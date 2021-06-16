from __future__ import  absolute_import,unicode_literals
from celery import task
from time import sleep

from django.template.loader import get_template
from .models import Link

@task()
def sleepy(duration):
    sleep(duration)
    return None

@task()
def msg():
    obj=Link.objects.all()
    for item in obj:
        item.save()

@task()
def msg1():
    print("hello world")



