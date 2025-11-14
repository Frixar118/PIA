from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('autos/', views.autos, name='autos'),
    path('eventos/', views.eventos, name='eventos'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('comentarios/', views.comentarios, name='comentarios'),


]
