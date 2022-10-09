

from django.urls import path
from translator import controller

urlpatterns = [
    path('upload', controller.upload_csv),
]