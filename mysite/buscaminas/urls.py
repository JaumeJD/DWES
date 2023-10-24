from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form_table', views.form_table, name="form_table")
]
