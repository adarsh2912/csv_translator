from django.urls import path
from translator import controller

urlpatterns = [
    path('upload', controller.upload_csv, name='upload'),
    path('translate/<str:id>/', controller.get_translated_data, name='translator')
]