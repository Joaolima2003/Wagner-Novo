from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('reserva/', views.CriarReservaView.as_view() , name='criar_reserva'),
    path('editar/<int:pk>/', views.EditarReservaView.as_view(), name='editar_reserva'),
    path('listar/', views.ListarReservasView.as_view(), name='listar_reserva'),
    path('deletar/<int:pk>/', views.DeletarReservaView.as_view(), name='deletar_reserva'),
    path('sucesso/', views.reserva_sucesso, name='reserva_sucesso'),
]



