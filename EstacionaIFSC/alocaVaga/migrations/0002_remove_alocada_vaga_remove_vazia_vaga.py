# Generated by Django 4.1.3 on 2022-12-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alocaVaga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alocada',
            name='vaga',
        ),
        migrations.RemoveField(
            model_name='vazia',
            name='vaga',
        ),
    ]
