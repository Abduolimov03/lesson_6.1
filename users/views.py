from django.shortcuts import render
from django.http import HttpResponse

def users(request):
    return HttpResponse('User lar bolimiga hush kelibsiz!')

def get_full_name(request):
    return HttpResponse('Abduolimov Asadbek')

