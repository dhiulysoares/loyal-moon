# Generated by Django 4.0 on 2022-01-04 19:48

from django.db import migrations
import localflavor.br.models
import program.models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_alter_indication_indicated_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=localflavor.br.models.BRCPFField(help_text='Formato: 11122233344', max_length=14, primary_key=True, serialize=False, unique=True, validators=[program.models.validate_indication_accepted], verbose_name='CPF '),
        ),
    ]
