from django.db import models

class AppBanco(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    celular = models.CharField(max_length=15, null=False, blank=False)
    cep = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=50, null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    localidade = models.CharField(max_length=50, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    datacadastro = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    concorda_whatsapp = models.BooleanField(default=False)  # Novo campo adicionado
    lideranca = models.CharField(max_length=50, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)  # Novo campo adicionado
