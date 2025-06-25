from django.urls import path

from .views import blog, new_blog

urlpatterns = [
    path('blog/', blog),
    path('new_blog/', new_blog),
]