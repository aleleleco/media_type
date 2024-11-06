from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.organiza_media.views import index



urlpatterns = [
  path('', index, name='index'),
  
] 
