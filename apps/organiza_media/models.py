
from django.db import models

class Imagem(models.Model):
    patch_arquivo = models.CharField(max_length=1000)
    nome_arquivo = models.CharField(max_length=255)
    data_captura_exif = models.CharField(max_length=255,null=True, blank=True)
    data_digitizacao_exif = models.CharField(max_length=255,null=True, blank=True)
    data_modificacao_exif = models.CharField(max_length=255,null=True, blank=True)
    data_modificacao = models.CharField(max_length=255,null=True, blank=True)
    timestamp_json = models.CharField(max_length=255,null=True, blank=True)
    formatted_json = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome_arquivo
