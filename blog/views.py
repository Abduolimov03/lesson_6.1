from django.shortcuts import render

from django.http import HttpResponse

def blog(request):
    return HttpResponse('Yangiliklar bolimiga hush kelibsiz!')
def new_blog(request):
    return HttpResponse('Jahon yangiliklari bilan tanishing')