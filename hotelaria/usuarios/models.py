from django.contrib.auth.models import AbstractUser
from django.db import models

class Hospede(AbstractUser):
    email = models.EmailField(unique=True)
  
    def __str__(self):
        return self.username

class TipoQuarto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_por_noite = models.DecimalField(max_digits=10, decimal_places=2)
  
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    data_check_in = models.DateField()
    data_check_out = models.DateField()
    tipo_quarto = models.ForeignKey(TipoQuarto, on_delete=models.CASCADE)
  
    def __str__(self):
        return f'Reserva de {self.hospede.username} - Quarto: {self.tipo_quarto.nome}'
