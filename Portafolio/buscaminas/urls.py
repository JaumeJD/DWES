from django.urls import path

from buscaminas import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crea_tablero', views.crea_tablero, name='crea_tablero')
]
