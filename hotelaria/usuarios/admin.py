from django.contrib import admin
from .models import Hospede,Reserva, TipoQuarto

admin.site.register(Hospede)
admin.site.register(Reserva)
admin.site.register(TipoQuarto)