from django import forms
from .models import AppBanco

class AppBancoForm(forms.ModelForm):
    class Meta:
        model = AppBanco
        fields = ['nome', 'celular', 'cep','bairro','endereco', 'complemento','localidade',
                  'uf','numero','data_nascimento','concorda_whatsapp','lideranca']
        widgets = {
            'cep': forms.TextInput(attrs={'id': 'id_cep'}),
            'endereco': forms.TextInput(attrs={'id': 'id_endereco'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento'}),
            'bairro': forms.TextInput(attrs={'id': 'id_bairro'}),
            'localidade': forms.TextInput(attrs={'id': 'id_localidade'}),
            'uf': forms.TextInput(attrs={'id': 'id_uf'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero'}),
            'nascimento': forms.TextInput(attrs={'id': 'id_datanascimento'}),
            'concorda_whatsapp': forms.CheckboxInput(attrs={'id': 'id_concorda_whatsapp'}),
            'lideranca': forms.TextInput(attrs={'id': 'id_lideranca'}),
            
        }
