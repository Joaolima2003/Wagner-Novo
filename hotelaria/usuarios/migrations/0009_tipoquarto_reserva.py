# Generated by Django 5.1.3 on 2024-11-29 03:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_remove_hospede_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoQuarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco_por_noite', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_check_in', models.DateField()),
                ('data_check_out', models.DateField()),
                ('hospede', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.tipoquarto')),
            ],
        ),
    ]
