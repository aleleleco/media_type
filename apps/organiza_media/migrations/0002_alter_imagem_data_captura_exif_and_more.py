# Generated by Django 5.1.2 on 2024-11-06 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiza_media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='data_captura_exif',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data_digitizacao_exif',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='data_modificacao_exif',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='timestamp_json',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
