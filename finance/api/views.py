from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

from .models import FinancialRecord

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        ## Validando existencia de usuario no banco
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuario cadastrado com este username')
        
        user = User.objects.create(username=username, email=email, password=password)
        user.save

        return HttpResponse('Usuáro Cadastrado com Sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)

            return render(request, 'homepage.html')
            
        else: 
            return HttpResponse('Email ou senha invalidos')
    
@login_required(login_url="login/")
def plataforma(request):
    return HttpResponse('plataforma')
    


def homepage(request):
    return render(request, 'homepage.html', {'page_title': 'Home Page'})


def accountingManagement(request):
    records = FinancialRecord.objects.all()
    return render(request, 'accountingManagement.html', {'page_title': 'Accounting Management','records': records})

def financialReport(request):
    return render(request, 'financialReport.html', {'page_title': 'Financial Reports'})


