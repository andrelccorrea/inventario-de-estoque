# Generated by Django 4.1.1 on 2022-11-28 02:06

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_configuracoesgerais_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="configuracoesgerais",
            name="logo_mini",
            field=models.ImageField(blank=True, null=True, upload_to="", verbose_name="logo mini"),
        ),
    ]
