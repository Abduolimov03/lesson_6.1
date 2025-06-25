from django.urls import path

from .views  import home, get_name

urlpatterns = [
    path('home/', home),
    path('name/', get_name),
]