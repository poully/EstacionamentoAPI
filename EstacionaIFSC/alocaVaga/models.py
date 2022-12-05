from django.db import models

class Alocada(models.Model):    
    placa = models.CharField('Placa',max_length=9)
    modelo = models.CharField('Modelo', max_length=15)

    def __str__(self):
        return self.vaga

class Vazia(models.Model):    
    placa = models.CharField('Placa',max_length=9)
    modelo = models.CharField('Modelo', max_length=15)

    def __str__(self):
        return self.vaga