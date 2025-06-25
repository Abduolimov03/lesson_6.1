from django.urls import path

from .views import users, get_full_name

urlpatterns = [
    path('users/', users),
    path('full_name/', get_full_name)
]