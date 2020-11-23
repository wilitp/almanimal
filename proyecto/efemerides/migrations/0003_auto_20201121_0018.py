# Generated by Django 3.0.8 on 2020-11-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efemerides', '0002_efemerides_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='efemerides',
            name='color',
            field=models.CharField(choices=[('warning', 'Amarillo'), ('primary', 'Azul'), ('info', 'Cian'), ('fuchsia', 'Fucsia'), ('orange', 'Naranja'), ('dark', 'Negro'), ('danger', 'Rojo'), ('success', 'Verde')], max_length=50, verbose_name='Color'),
        ),
    ]