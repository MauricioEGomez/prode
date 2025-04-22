from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from base.models import Usuario
# Create your views here.


def home(request):
    return render(request, 'home.html'
                  )

def signup(request):
    if request.method == 'GET':
        # print('mostrando formulario')
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        print(request.POST)
        # print('obteniendo datos')
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                usuario = Usuario.objects.create(nombre=request.POST['username'])
                usuario.save()
                login(request,user)
                return redirect('home')
            # except Exception as e:
            #     print('Error inesperado: ' + str(e))
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya fue creado previamente"
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': "Los passwords no coinciden"
            })

def login_view(request):
    if request.method == 'GET':
        # print('mostrando formulario')
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # print('obteniendo datos')
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else: 
                login(request,user)
                return redirect('home')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')