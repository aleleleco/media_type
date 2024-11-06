from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import apps.organiza_media.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apps.organiza_media.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

