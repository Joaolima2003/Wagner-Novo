# Generated by Django 5.1.3 on 2024-11-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospede',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
