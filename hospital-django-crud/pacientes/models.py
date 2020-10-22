from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Paciente(models.Model):
    nome = models.CharField(max_length=80)
    telefone = PhoneNumberField()
    email = models.EmailField(max_length=50)
    dtNascimento = models.DateField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
            return self.nome
            

