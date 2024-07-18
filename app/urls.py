from django.urls import path
from .views import create_appbanco

urlpatterns = [
    path('appbanco/', create_appbanco, name='appbanco'),

    # Adicione outras URLs aqui
]
