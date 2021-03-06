# Generated by Django 3.0.8 on 2020-11-16 18:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_paginaadopcion_paginablog_paginacontacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginadonaciones',
            name='description',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Texto'),
        ),
        migrations.AddField(
            model_name='paginainicio',
            name='description',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='paginaadopcion',
            name='seo_description',
            field=models.CharField(max_length=255, verbose_name='SEO'),
        ),
        migrations.AlterField(
            model_name='paginablog',
            name='seo_description',
            field=models.CharField(max_length=255, verbose_name='SEO'),
        ),
        migrations.AlterField(
            model_name='paginacontacto',
            name='seo_description',
            field=models.CharField(max_length=255, verbose_name='SEO'),
        ),
        migrations.AlterField(
            model_name='paginadonaciones',
            name='seo_description',
            field=models.CharField(max_length=255, verbose_name='SEO'),
        ),
        migrations.AlterField(
            model_name='paginainicio',
            name='seo_description',
            field=models.CharField(max_length=255, verbose_name='SEO'),
        ),
    ]
