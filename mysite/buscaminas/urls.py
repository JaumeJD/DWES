from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_form', views.create_form, name="create_form"),
]
