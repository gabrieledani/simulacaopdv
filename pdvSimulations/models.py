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
    tipo_simulacao = models.IntegerField(choices=((0, "NENHUM"),(1, "MENSAL"),(2, "TRIMESTRAL"),(3, "DIA DAS MAES"),(4, "DIA DOS PAIS"),(5, "NATAL"),(6, "BLACK FRIDAY"),(7, "ANIVERSARIO CLIENTE"),(8, "BONUS PERFORMACE")),default=0)
    tipo_evento = models.IntegerField(choices=((0, "NENHUM"),(1, "DESCONTOS ESCALONADOS 2% "), (2, "DESCONTOS ESCALONADOS 5% GER"), (3, "DESCONTOS ESCALONADOS 7% GER"), (4, "10/11 - 9,10%"), (5, "12/13 - 7,69%"),(6, "20/01 - 4,80%"),(7, "BÔNUS 1%"),(8, "BÔNUS 2%"),(9, "PRAZO - 2% (30 DIAS)"),(10, "PRAZO - 4% (60 DIAS)"),(11, "PRAZO - 6% (90 DIAS)"),(11, "VERBA VALOR FECHADO)")),default=0)
    txt_verba1 = models.CharField(max_length=20,blank=True)
    vlr_verba1 = models.FloatField(null=True, blank=True, default=0.0)
    txt_verba2 = models.CharField(max_length=20,blank=True)
    vlr_verba2 = models.FloatField(null=True, blank=True, default=0.0)
    txt_verba3 = models.CharField(max_length=20,blank=True)
    vlr_verba3 = models.FloatField(null=True, blank=True, default=0.0)
    txt_verba4 = models.CharField(max_length=20,blank=True)
    vlr_verba4 = models.FloatField(null=True, blank=True, default=0.0)
    txt_verba5 = models.CharField(max_length=20,blank=True)
    vlr_verba5 = models.FloatField(null=True, blank=True, default=0.0)
    
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