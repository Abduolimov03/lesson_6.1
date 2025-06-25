from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('salom homee')
def get_name(request):
    return HttpResponse('Salom Asadbek')