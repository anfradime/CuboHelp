from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Registro de usuario
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirigir a la página principal
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# Inicio de sesión
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirigir después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def home(request):
    return render(request, 'helpdesk/home.html')

# Cierre de sesión
def user_logout(request):
    logout(request)
    return redirect("home")  # Redirigir a la página principal

