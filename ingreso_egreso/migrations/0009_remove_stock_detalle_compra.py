# Generated by Django 4.1.7 on 2023-10-14 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso_egreso', '0008_alter_detalle_venta_precio_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='detalle_compra',
        ),
    ]
