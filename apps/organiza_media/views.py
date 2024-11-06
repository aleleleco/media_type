from django.shortcuts import render
from .models import Imagem
import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import json


# Create your views here.
def index(request):
    
    if request.method == 'POST':
        print('pegou post')
        pasta_origem = request.POST['pasta_origem']
        pasta_destino = request.POST['pasta_destino']
        selected_media_types = request.POST.getlist('tipos_media')
        apagar_arquivos = request.POST.get('apagar_arquivos')

        # pega os arquivos na pasta de origem
        lista_arquivos = checa_arquivos (pasta_origem, pasta_destino, selected_media_types)
        
        #verificar arquivos de imagem

        lista_arquivos = verifica_exif(lista_arquivos)
        lista_arquivos = busca_jason(lista_arquivos)
        grava_banco(lista_arquivos)
            

    return render(request, 'index.html')


def checa_arquivos(pasta_origem, pasta_destino, selected_media_types):
    lista_arquivos = []
    for raiz, diretorios, arquivos in os.walk(pasta_origem):
        for arquivo in arquivos:
            if arquivo.endswith(tuple(selected_media_types)):
                lista_arquivos.append((raiz, arquivo))
            
    return lista_arquivos


def verifica_exif(lista_arquivos):
    lista_arquivos_exif = []
    for arquivo in lista_arquivos:
        try:
            print('--------')
            image = Image.open(arquivo[0] + '/' + arquivo[1])
            exif_data = image.getexif()
            
            data_modificacao = datetime.fromtimestamp(os.path.getmtime(arquivo[0] + '/' + arquivo[1]))
            
            # Capturando as datas EXIF
            data_captura = exif_data.get(36867)  # DateTimeOriginal
            data_digitizacao = exif_data.get(36868)  # DateTimeDigitized
            data_exif_modificacao = exif_data.get(306)  # DateTime
            
                        
        except Exception as e:
            print(f"Erro ao processar {arquivo[1]}: {e}")
            data_captura = None
            data_digitizacao = None
            data_exif_modificacao = None
            data_modificacao = None
        
        lista_arquivos_exif.append((arquivo[0], arquivo[1], data_captura, data_digitizacao, data_exif_modificacao, data_modificacao))
    
    return lista_arquivos_exif


def busca_jason(lista_arquivos):
    lista_json = []
    for arquivo in lista_arquivos:
        try:
            with open(f'{arquivo[0]}/{arquivo[1]}.json', 'r') as arquivo_json:

                arquivo_json = json.load(arquivo_json)
                timestamp = arquivo_json['photoTakenTime']['timestamp']
                formatted = arquivo_json['photoTakenTime']['formatted']

                lista_json.append((arquivo[0], arquivo[1], arquivo[2], arquivo[3], arquivo[4], arquivo[5], timestamp, formatted))
        except FileNotFoundError:
            print(f"Arquivo JSON não encontrado para {arquivo[1]}")
            lista_json.append((arquivo[0], arquivo[1], arquivo[2], arquivo[3], arquivo[4], arquivo[5], None, None))
    return lista_json

def grava_banco(lista_arquivos):
    
    for arquivo in lista_arquivos:
        imagem = Imagem(
            patch_arquivo=arquivo[0],
            nome_arquivo=arquivo[1],
            data_captura_exif=arquivo[2],
            data_digitizacao_exif=arquivo[3],
            data_modificacao_exif=arquivo[4],
            data_modificacao=arquivo[5],
            timestamp_json=arquivo[6],
            formatted_json=arquivo[7]
        )
        imagem.save()