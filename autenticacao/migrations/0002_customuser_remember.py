# Generated by Django 4.1.1 on 2022-11-27 19:07

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("autenticacao", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="remember",
            field=models.BooleanField(default=True, verbose_name="lembrar-me"),
        ),
    ]
