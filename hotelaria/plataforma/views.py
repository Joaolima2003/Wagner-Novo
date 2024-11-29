from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from usuarios.models import Reserva 
from usuarios.forms import ReservaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView

@login_required
def home(request):
    return render(request, 'home.html')


class CriarReservaView(LoginRequiredMixin, CreateView): 
    model = Reserva 
    form_class = ReservaForm
    template_name = 'criar_reserva.html' 
    success_url = reverse_lazy('reserva_sucesso') #reserva sucesso
    login_url = 'login'
    redirect_field_name = 'next'
    
    
    def form_valid(self, form):
        form.instance.hospede = self.request.user
        messages.success(self.request, "Reserva criada com sucesso!") 
        return super().form_valid(form) 
    
   
    

class EditarReservaView(LoginRequiredMixin, UpdateView): 
    model = Reserva 
    form_class = ReservaForm 
    template_name = 'editar_reserva.html' 
    success_url = reverse_lazy('reserva_sucesso') 
    login_url = 'login'


    def get_queryset(self):
        queryset = super().get_queryset() 
        return queryset.filter(hospede=self.request.user) 
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object() 
        if obj.hospede != self.request.user:
            messages.danger(request, "Você não tem permissão para editar esta reserva.") 
        return super().dispatch(request, *args, **kwargs) 
    

class ListarReservasView(LoginRequiredMixin, ListView): 
    model = Reserva 
    template_name = 'listar_reserva.html' 
    context_object_name = 'reservas' 
    
    def get_queryset(self): 
       return Reserva.objects.filter(hospede=self.request.user)



class DeletarReservaView(LoginRequiredMixin, DeleteView):
    model = Reserva 
    template_name = 'deletar_reserva.html'
    success_url = reverse_lazy('listar_reserva')
    login_url = 'login' 
    redirect_field_name = 'next'
    
    def get_queryset(self): 
        return Reserva.objects.filter(hospede=self.request.user)



@login_required
def reserva_sucesso(request): 
    return render(request, 'reserva_sucesso.html')






    
