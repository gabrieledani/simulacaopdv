from django import forms
from .models import Simulacao,Itens_Simulacao

class NovaSimulacao(forms.ModelForm):
    tipo_simulacao = forms.ChoiceField(label="Evento Nome:", initial='',widget=forms.Select(attrs={'class':'form-select'}),
                choices=((0, "NENHUM"),(1, "MENSAL"), (2, "TRIMESTRAL"), (3, "DIA DAS MÃES"), (4, "DIA DOS PAIS"), (5, "NATAL"),(6, "BLACK FRIDAY"),(7, "ANIVERSARIO CLIENTE"),(8, "BONUS PERFORMACE")), required=True)

    tipo_evento = forms.ChoiceField(label="Evento Tipo:", initial='',widget=forms.Select(attrs={'class':'form-select'}),
                choices=((0, "NENHUM"),(1, "DESCONTOS ESCALONADOS 2% "), (2, "DESCONTOS ESCALONADOS 5% GER"), (3, "DESCONTOS ESCALONADOS 7% GER"), (4, "10/11 - 9,10%"), (5, "12/13 - 7,69%"),(6, "20/01 - 4,80%"),(7, "BÔNUS 1%"),(8, "BÔNUS 2%"),(9, "PRAZO - 2% (30 DIAS)"),(10, "PRAZO - 4% (60 DIAS)"),(11, "PRAZO - 6% (90 DIAS)"),(11, "VERBA VALOR FECHADO)")), required=True)
    
    class Meta:
        model = Simulacao
        fields = ('dt_simulacao','cod_rep','cod_cliente','cod_empr','aprovada','observacao','tipo_simulacao','tipo_evento','txt_verba1','vlr_verba1','txt_verba2','vlr_verba2','txt_verba3','vlr_verba3','txt_verba4','vlr_verba4','txt_verba5','vlr_verba5')
        labels = {
            'dt_simulacao':'Data:',
            'cod_rep':'Representante:',
            'cod_cliente':'Cliente:',
            'cod_empr':'Empresa:',
            'aprovada':'Aprovada:',
            'observacao':'Observação:',
            'txt_verba1':'Verba Adicional 1:',
            'vlr_verba1':'Valor:',
            'txt_verba2':'Verba Adicional 2:',
            'vlr_verba2':'Valor:',
            'txt_verba3':'Verba Adicional 3:',
            'vlr_verba3':'Valor:',
            'txt_verba4':'Verba Adicional 4:',
            'vlr_verba4':'Valor:',
            'txt_verba5':'Verba Adicional 5:',
            'vlr_verba5':'Valor:'
        }
        widgets = {
            'dt_simulacao':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'cod_rep':forms.NumberInput(attrs={'class':'form-control'}),
            'cod_cliente':forms.NumberInput( attrs={'class':'form-control'}),
            'cod_empr':forms.NumberInput(attrs={'class':'form-control'}),
            'aprovada':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'observacao':forms.Textarea(attrs={'class':'form-control'}),
            'txt_verba1':forms.TextInput(attrs={'class':'form-control'}),
            'vlr_verba1':forms.NumberInput(attrs={'class':'form-control '}),
            'txt_verba2':forms.TextInput(attrs={'class':'form-control'}),
            'vlr_verba2':forms.NumberInput(attrs={'class':'form-control'}),
            'txt_verba3':forms.TextInput(attrs={'class':'form-control'}),
            'vlr_verba3':forms.NumberInput(attrs={'class':'form-control'}),
            'txt_verba4':forms.TextInput(attrs={'class':'form-control'}),
            'vlr_verba4':forms.NumberInput(attrs={'class':'form-control'}),
            'txt_verba5':forms.TextInput(attrs={'class':'form-control'}),
            'vlr_verba5':forms.NumberInput(attrs={'class':'form-control'})
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
