from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import HospedeForm, LoginForm
from django.contrib.auth import logout

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = HospedeForm(request.POST)
        if form.is_valid():
            hospede = form.save(commit=False)
            hospede.password = make_password(form.cleaned_data['password'])
            hospede.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = HospedeForm()
    return render(request, 'cadastrar_hospede.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request,'Login realizado com sucesso!')
                return redirect('home')
            else:
                messages.warning(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = LoginForm()

    return render(request, 'login_hospede.html', {'form': form})

def logout_view(request):
    request.session.flush()
    logout(request)
    messages.success(request, 'Você foi deslogado com sucesso.')
    return redirect('login')