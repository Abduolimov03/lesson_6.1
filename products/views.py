from django.shortcuts import render

from django.http import HttpResponse

def product(request):
    return HttpResponse('Mahsulotlar bolimiga hush kelibsiz')
def basket(request):
    return HttpResponse('Mahsulotlaringizni korishingiz mumkin')