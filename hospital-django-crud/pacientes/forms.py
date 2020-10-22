from django import forms
from .models import Paciente

class PacienteForms(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome', 'telefone', 'email', 'endereco', 'dtNascimento')
        labels = {
            'nome': 'Nome',
            'email': 'E-Mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'dtNascimento': 'Data de Nasc.'
        }