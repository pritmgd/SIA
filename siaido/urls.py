from django.urls import path
from . import views

app_name = 'siaido'
urlpatterns = [
    path('', views.index, name='index'),
    path('portal/', name='portal'),
]