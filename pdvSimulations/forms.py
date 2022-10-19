from django import forms
from .models import Simulacao,Itens_Simulacao

class NovaSimulacao(forms.ModelForm):
    class Meta:
        model = Simulacao
        fields = ('dt_simulacao','cod_rep','cod_cliente','cod_empr')#,'situacao')
        labels = {
            'dt_simulacao':'Data:',
            'cod_rep':'Representante:',
            'cod_cliente':'Cliente:',
            'cod_empr':'Empresa:'
            #'situacao':'Ativo'
        }
        widgets = {
            'dt_simulacao':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'cod_rep':forms.NumberInput(attrs={'class':'form-control'}),
            'cod_cliente':forms.NumberInput( attrs={'class':'form-control'}),
            'cod_empr':forms.NumberInput(attrs={'class':'form-control'})
            #'situacao':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class NovoItem(forms.ModelForm):
    class Meta:
        model = Itens_Simulacao
        fields = ('cod_item','cod_mascara','qtde','valor','ean_item')#,'situacao')
        labels = {
            'cod_item':'Item:',
            'cod_mascara':'Máscara:',
            'qtde':'Qtde:',
            'valor':'Valor:',
            'ean_item':'EAN13:'
            #'situacao':'Ativo'
        }
        widgets = {
            'cod_item':forms.TextInput(attrs={'class':'form-control'}),
            'cod_mascara':forms.TextInput(attrs={'class':'form-control'}),
            'qtde':forms.NumberInput( attrs={'class':'form-control'}),
            'valor':forms.NumberInput(attrs={'class':'form-control'}),
            'ean_item':forms.TextInput(attrs={'class':'form-control'})
            #'situacao':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
