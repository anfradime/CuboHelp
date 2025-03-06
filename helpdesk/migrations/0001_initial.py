# Generated by Django 5.1.6 on 2025-03-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('en_progreso', 'En Progreso'), ('cerrado', 'Cerrado')], default='abierto', max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
