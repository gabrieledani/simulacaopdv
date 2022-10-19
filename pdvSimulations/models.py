from email.policy import default
from django.db import models

class Simulacao(models.Model):
    #cod_simulacao = models.IntegerField()
    dt_simulacao = models.DateField()
    cod_rep = models.IntegerField()
    cod_cliente = models.IntegerField()
    cod_empr = models.IntegerField(default=1)
    situacao = models.BooleanField(default=True)
    
    # def __str__(self):
    #     return self.cod_simulacao

class Itens_Simulacao(models.Model):
    simulacao = models.ForeignKey(Simulacao,on_delete=models.CASCADE)

    cod_item = models.CharField(max_length=20)
    cod_mascara = models.CharField(max_length=20,blank=True)
    qtde = models.IntegerField()
    valor = models.FloatField()
    ean_item = models.CharField(max_length=20)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.ean_item