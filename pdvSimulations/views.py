from django.shortcuts import render, redirect
from .models import Simulacao,Itens_Simulacao
from .forms import NovaSimulacao,NovoItem

def simulations(request):
    print('TODAS')
    todas_simulacoes = Simulacao.objects.all().order_by('-id')
    return render(request, 'index.html',{'title':'Simulações de Pedido','todas_simulacoes':todas_simulacoes})


def new_simulation(request):
    print('NOVA')
    if request.method == 'POST':
        print('post de nova simulação?,não sei')
        form = NovaSimulacao(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('simulations')
    else:
        form = NovaSimulacao()
        return render(request, 'simulations.html',{'title':'Nova Simulação de Pedido','form': form})


def delete_simulation(request, simulation_id):
    print('APAGA')
    simulacao = Simulacao.objects.get(pk=simulation_id)
    simulacao.delete()
    return redirect('simulations')


def edit_simulation(request, simulation_id):
    print('EDITA')
    if request.method == 'POST':
        simulacao = Simulacao.objects.get(pk=simulation_id)
        form = NovaSimulacao(request.POST or None, instance=simulacao)
        if form.is_valid():
            form.save()
        return redirect('simulations')
    else:
        simulacao = Simulacao.objects.get(pk=simulation_id)
        form = NovaSimulacao(instance=simulacao)
        return render(request, 'simulations.html',{'title':'Editando uma Simulação','simulacao':simulacao,'form': form})


def simulation_items(request, simulation_id):
    simulacao = Simulacao.objects.get(pk=simulation_id)
    if request.method == 'POST':
        form = NovoItem(request.POST or None)
        if form.is_valid():
            item_simulacao = form.save(commit=False)
            item_simulacao.simulacao_id = simulation_id
            form.save()
    form = NovoItem()
    lista_itens = Itens_Simulacao.objects.filter(simulacao_id=simulation_id).order_by('-id')
    return render(request, 'simulation_items.html',{'title':'Novo Item da Simulação','simulacao':simulacao,'form': form,'lista_itens':lista_itens})

def delete_items(request, item_id):
    item = Itens_Simulacao.objects.get(pk=item_id)
    item.delete()
    return redirect('simulation_items',item.simulacao.pk)

def edit_items(request, item_id):
    item = Itens_Simulacao.objects.get(pk=item_id)
    simulacao = Simulacao.objects.get(pk=item.simulacao.pk)
    if request.method == 'POST':
        form = NovoItem(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
    else:
        item = Itens_Simulacao.objects.get(pk=item_id)
        form = NovoItem(instance=item)
    lista_itens = Itens_Simulacao.objects.filter(simulacao_id=item.simulacao)
    return render(request, 'simulation_items.html',{'title':'Editando um Item da Simulação','simulacao':simulacao,'item':item,'form': form,'lista_itens':lista_itens})
