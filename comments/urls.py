from django.urls import path

from .views import comments, write_comment

urlpatterns = [
    path('comments/', comments),
    path('write_comment/', write_comment),
]