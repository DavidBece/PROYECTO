# Generated by Django 4.1.7 on 2023-05-25 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=45, verbose_name='Dirección')),
                ('municipio', models.CharField(max_length=45, verbose_name='Municipio')),
                ('telefono', models.CharField(max_length=45, verbose_name='Telefono')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=45, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, unique=True, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=45, verbose_name='Apellido')),
                ('contraseña', models.CharField(max_length=45, verbose_name='Contraseña')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extrangería')], max_length=2, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=45, verbose_name='Documento')),
                ('telefono', models.CharField(max_length=45, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=45, verbose_name='Dirección')),
                ('correo', models.CharField(max_length=45, verbose_name='Correo')),
                ('rol', models.CharField(choices=[('Admin', 'Administrador'), ('Empleado', 'Empleado'), ('Usuario', 'Usuario')], max_length=10, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=45, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Usuario_has_Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idsucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.sucursal', verbose_name='ID Sucursal')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='ID Usuario')),
            ],
        ),
    ]
