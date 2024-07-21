from django.urls import path
from .views import create_appbanco, relatorio_dados

urlpatterns = [
    path('appbanco/', create_appbanco, name='appbanco'),
    path('relatorio/', relatorio_dados, name='relatorio')

    # Adicione outras URLs aqui
]
