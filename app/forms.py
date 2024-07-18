# forms.py

from django import forms
from .models import AppBanco


class AppBancoForm(forms.ModelForm):
    class Meta:
        model = AppBanco
        fields = ['nome', 'celular', 'cep', 'endereco', 'complemento', 'bairro', 'localidade', 'uf', 'numero']
        widgets = {
            'cep': forms.TextInput(attrs={'id': 'id_cep'}),
            'endereco': forms.TextInput(attrs={'id': 'id_endereco', 'disabled': 'disabled'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento', 'disabled': 'disabled'}),
            'bairro': forms.TextInput(attrs={'id': 'id_bairro', 'disabled': 'disabled'}),
            'localidade': forms.TextInput(attrs={'id': 'id_localidade', 'disabled': 'disabled'}),
            'uf': forms.TextInput(attrs={'id': 'id_uf', 'disabled': 'disabled'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero', 'disabled': 'disabled'}),
        }
