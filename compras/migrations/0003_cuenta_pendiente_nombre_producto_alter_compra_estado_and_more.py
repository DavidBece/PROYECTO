# Generated by Django 4.2.1 on 2023-06-29 21:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_alter_categoria_estado_alter_categoria_nombre_and_more'),
        ('usuarios', '0003_alter_sucursal_direccion_alter_sucursal_estado_and_more'),
        ('compras', '0002_alter_cuenta_pendiente_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta_pendiente',
            name='nombre_producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Nombre del Producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compra',
            name='estado',
            field=models.CharField(blank=True, choices=[('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='idcuentapendiente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='compras.cuenta_pendiente', verbose_name='Cuenta Pendiente'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='idusuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='cuenta_pendiente',
            name='estado',
            field=models.CharField(blank=True, choices=[('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='cuenta_pendiente',
            name='nombre',
            field=models.CharField(blank=True, max_length=45, validators=[django.core.validators.RegexValidator('^[A-Za-z]+$', message='Este campo solo permite letras.')]),
        ),
        migrations.AlterField(
            model_name='cuenta_pendiente',
            name='valor',
            field=models.IntegerField(blank=True, max_length=45, verbose_name='Valor'),
        ),
    ]
