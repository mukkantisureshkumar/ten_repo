from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('topic is created')

def insert_webpage(request):
    '''
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    '''
    tn=input('enter topic_name:')
    n=input('enter name:')
    u=input('enter url:')
    e=input('enter email:')
    TO=Topic.objects.filter(topic_name=tn)[0]
    if TO:    
        na=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        na.save()
        return HttpResponse('Webpage is created')
    else:
        return HttpResponse('Given Topic is Not present in My Parent Table')


def insert_accessrecord(request): 
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    
    n=input('enter name:')
    u=input('enter url:')
    e=input('enter email:')
    na=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
    na.save()
    
    d=input('enter date:')
    a=input('enter author:')
    ac=AccessRecord.objects.get_or_create(name=na,date=d,author=a)[0]
    ac.save()
    return HttpResponse('accessrecord is created')
    





