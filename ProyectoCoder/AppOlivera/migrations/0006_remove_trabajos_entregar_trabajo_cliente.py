# Generated by Django 4.2.5 on 2023-09-12 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppOlivera", "0005_tipo_servicio_tipo_servicio"),
    ]

    operations = [
        migrations.RemoveField(model_name="trabajos_entregar", name="trabajo_cliente",),
    ]