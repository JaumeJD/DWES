from django.urls import path
from buscaminas import views

urlpatterns = [
    path('', views.index, name="index"),
]
