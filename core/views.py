from django.shortcuts import render
from .forms import Contactform, ProdutoModelForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def contact(request):
    form = Contactform(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():         #retorna TRUE se não tiver erro
            form.send_mail()        #envia o email
            messages.success(request,'E-mail enviado com sucesso')
            form = Contactform()        #limpa o formulario apos tudo.
        else:
            messages.error(request,'Erro ao enviar o e-mail')
    context = {
        'formulario' : form
    }

    return render(request, 'contact.html',context)


def product(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request,'Produto salvo com sucesso. ')
            form = ProdutoModelForm()
        else:
            messages.error(request,'Erro ao salvar o produto')
    else:
        form = ProdutoModelForm()
    context = {
            'form' : form
        }
    return render(request, 'product.html',context)


