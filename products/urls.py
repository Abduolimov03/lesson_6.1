from django.urls import path

from .views import product, basket

urlpatterns = [
    path('product/', product),
    path('basket/', basket),
]