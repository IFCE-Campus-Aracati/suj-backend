# Generated by Django 5.1.1 on 2024-09-21 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jogos", "0002_modalidade_categoria_modalidade_tipo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="equipes",
            name="jogadores",
        ),
    ]
