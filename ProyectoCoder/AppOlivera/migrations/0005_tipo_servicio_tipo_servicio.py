# Generated by Django 4.2.5 on 2023-09-11 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppOlivera", "0004_tipo_servicio_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="tipo_servicio",
            name="tipo_servicio",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
