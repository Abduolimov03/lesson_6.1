from django.shortcuts import render

from django.http import HttpResponse

def comments(request):
    return HttpResponse('Commentlar bolimiga hush kelibsiz')
def write_comment(request):
    return HttpResponse('Comment yozing')