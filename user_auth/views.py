from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_auth.my_forms import LoginForm
from user_auth.my_forms import RegisterUserForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('core:index')
        else:
            messages.success(request, "Usuário ou senha inválidos!")
            form = LoginForm()
            return render(request, 'login_user.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login_user.html', {'form': form})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('user_auth:login_user')

@login_required
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # In other scenarios, the ideal would be for the user to be logged in after being registered. However, since this system is not a common system where users can register at will, I chose to keep the user who registered the other logged in
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1'] # password1 is the first box to fill in. On the other hand, password2 is the second box to fill in, referring to password confirmation
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('core:index')
        else:
            form = RegisterUserForm(request.POST)
            return render(request, 'register_user.html', {'form': form})
    else:
        form = RegisterUserForm()   
    return render(request, 'register_user.html', {'form': form})