from django.contrib import admin
from django.urls import path, include
from app.views import index  # Importe a view 'index' do seu aplicativo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Associa a view 'index' ao nome 'index'
    path('app/', include('app.urls')),  # Inclui as URLs do seu aplicativo (substitua 'app' pelo nome do seu aplicativo)
]
