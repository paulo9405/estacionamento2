from django.shortcuts import render, redirect
import csv
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

from .forms import (
    PessoaForm, 
    VeiculoForm,
    MovRotativosForm,
    MensalistaForm,
    MovMensalistaForm
)

@login_required()
def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)


@login_required()
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required()
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required()
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required()
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


@login_required()
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data =  {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


@login_required()
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required()
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required()
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


@login_required()
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativosForm()
    data =  {'mov_rot': mov_rot, 'form': form}
    return render(
        request, 'core/lista_movrotativos.html', data)


@login_required()
def movrotativos_novo(request):
    form = MovRotativosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required()
def movrotativos_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativosForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativos.html', data)


@login_required()
def movrotativos_delete(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_rotativo})


@login_required()
def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(
        request, 'core/lista_mensalistas.html', data)


@login_required()
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


@login_required()
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required()
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


@login_required()    
def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'form': form}
    return render(
        request, 'core/lista_movmensalistas.html', data)


@login_required()
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')


@login_required()
def movmensalista_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/update_movmensalista.html', data)


@login_required()
def movmensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_mensalista})

#PDFs------------------------------------------------------------------------------------------
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf_veiculos(View):
    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio-veiculos.html', params, 'relatorio_veiculos')


class Pdf_pessoas(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        params = {
            'pessoas': pessoas,
            'request': request,
        }
        return Render.render('core/relatorio-pessoas.html', params, 'relatorio_pessoas')


class Pdf_movrotativo(View):
    def get(self, request):
        mov_rot = MovRotativo.objects.all()
        params = {
            'mov_rot': mov_rot,
            'request': request,
        }
        return Render.render('core/relatorio-movrotativo.html', params, 'relatorio_movrotativo')


class Pdf_mensalistas(View):
    def get(self, request):
        mensalistas = Mensalista.objects.all()
        params = {
            'mensalistas': mensalistas,
            'request': request,
        }
        return Render.render('core/relatorio-mensalistas.html', params, 'relatorio_mensalistas')


class CSV_veiculos(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="veiculos.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response
    

class CSV_pessoas(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pessoas.csv"'

        pessoas = Pessoa.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Nome', 'Endereço', 'Telefone'])

        for pessoa in pessoas:
            writer.writerow(
                [pessoa.id, pessoa.nome, pessoa.endereco, pessoa.telefone])

        return response


class CSV_movrotativo(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="movrotativo.csv"'

        mov_rot = MovRotativo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Checkin', 'Checkout', 'Valor', 'Veiculo'])

        for mov in mov_rot:
            writer.writerow(
                [mov.id, mov.checkin, mov.checkout, mov.valor_hora, mov.veiculo])

        return response


class CSV_mensalistas(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mensalistas.csv"'

        mensalistas = Mensalista.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Veiculo', 'Inicio', 'Valor'])

        for mensalista in mensalistas:
            writer.writerow(
                [mensalista.id, mensalista.veiculo, mensalista.inicio, mensalista.valor_mes])

        return response