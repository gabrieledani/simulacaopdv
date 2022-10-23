from django.db import models

class Simulacao(models.Model):
    #cod_simulacao = models.IntegerField()
    dt_simulacao = models.DateField()
    cod_rep = models.IntegerField()
    cod_cliente = models.IntegerField()
    cod_empr = models.IntegerField(default=1)
    situacao = models.BooleanField(default=True)
    aprovada = models.BooleanField(default=False)
    observacao = models.CharField(max_length=200,blank=True)
    tipo_simulacao = models.IntegerField(choices=((1, "Tipo1"),(2, "Tipo2"),(3, "Tipo3"),(4, "Tipo4"),(5, "Outro")),default=1)
    txt_verba1 = models.CharField(max_length=20,blank=True)
    vlr_verba1 = models.FloatField(null=True)
    txt_verba2 = models.CharField(max_length=20,blank=True)
    vlr_verba2 = models.FloatField(null=True)
    txt_verba3 = models.CharField(max_length=20,blank=True)
    vlr_verba3 = models.FloatField(null=True)
    txt_verba4 = models.CharField(max_length=20,blank=True)
    vlr_verba4 = models.FloatField(null=True)
    txt_verba5 = models.CharField(max_length=20,blank=True)
    vlr_verba5 = models.FloatField(null=True)
    
    # def __str__(self):
    #     return self.cod_simulacao

class Itens_Simulacao(models.Model):
    simulacao = models.ForeignKey(Simulacao,on_delete=models.CASCADE)

    cod_item = models.CharField(max_length=20)
    cod_mascara = models.CharField(max_length=20,blank=True)
    qtde = models.IntegerField()
    valor = models.FloatField()
    ean_item = models.CharField(max_length=20,blank=True)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return self.cod_item