# Generated by Django 4.2 on 2023-05-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_rename_hora_reserva_horario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="data",
            field=models.DateField(),
        ),
    ]
