from django.db import models
from localflavor.br.models import BRCPFField
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Nome')
    cpf = BRCPFField('CPF ', blank=False, primary_key=True, help_text='Formato: 00011122233')
    phone = PhoneNumberField(region='BR', blank=False, help_text='Formato DDD + Número', verbose_name='Telefone')
    email = models.EmailField(max_length=255, blank=False)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        details = f'Cliente: {self.name} | cpf: {self.cpf}'
        return details

class Indication(models.Model):
    source_cpf = BRCPFField('CPF do usuário indicador', blank=False, unique=False)
    target_cpf = BRCPFField('CPF do usuário indicado', blank=False, unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        details = f'Indicante: {self.source_cpf} | Indicado: {self.target_cpf}| Data: {self.date}'
        return details
