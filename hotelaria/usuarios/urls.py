from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('sair/', views.logout_view, name='logout_view'),
]

