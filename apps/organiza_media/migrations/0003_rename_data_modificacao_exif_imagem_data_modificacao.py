# Generated by Django 5.1.2 on 2024-11-06 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organiza_media', '0002_alter_imagem_data_captura_exif_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagem',
            old_name='data_modificacao_exif',
            new_name='data_modificacao',
        ),
    ]