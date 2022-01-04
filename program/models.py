from django.db import models
from localflavor.br.models import BRCPFField
#from phonenumber_field.modelfields import PhoneNumberField
from localflavor.exceptions import ValidationError


def validate_cpf_indicated(cpf_value):
    if Client.objects.filter(cpf=cpf_value).exists():
        raise ValidationError('cpf invalido')

def validate_exists_another_indication(cpf_value):
    if Indication.objects.filter(indicated_cpf=cpf_value).exists():
        raise ValidationError('cpf invalido')

class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Nome')
    cpf = BRCPFField('CPF ', blank=False, primary_key=True, help_text='Formato: 00011122233', unique=True)
    #phone = PhoneNumberField(region='BR', blank=False, help_text='Formato DDD + Número', verbose_name='Telefone') #TODO fix it
    email = models.EmailField(max_length=255, blank=False)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        details = f'Cliente: {self.name} | cpf: {self.cpf}'
        return details


class Indication(models.Model):
    PENDING_STATUS = 1
    ACCEPT_STATUS = 2
    CANCELED_STATUS = 3
    STATUS_CHOICES = (
        (PENDING_STATUS, 'Pendente'),
        (ACCEPT_STATUS, 'Aceita'),
        (CANCELED_STATUS, 'Cancelada'),
    )
    status = models.IntegerField(default=PENDING_STATUS)
    client_cpf = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING, related_name='client_cpf',
        blank=False, unique=False, verbose_name='Cliente')
    indicated_cpf = BRCPFField('CPF indicado', blank=False, unique=False, validators=[validate_cpf_indicated])
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        details = f'Indicante: {self.client_cpf} | Indicado: {self.indicated_cpf}| Data: {self.creation_date}'
        return details
