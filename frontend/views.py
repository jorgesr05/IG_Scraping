from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.utils.decorators import method_decorator
import requests


def home(request):
    return render(request, "frontend/home.html")

# @login_required


def dashboard(request):  # 🔥 Asegurar que 'request' está presente
    return render(request, "frontend/dashboard.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        response = requests.post("http://127.0.0.1:8000/api/token/", json={
            "username": username,
            "password": password
        })

        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get("access")
            refresh_token = token_data.get("refresh")

            if access_token:
                # Guardar tokens en la sesión de Django
                request.session["access_token"] = access_token
                request.session["refresh_token"] = refresh_token
                # Para mostrarlo en la UI
                request.session["username"] = username
                messages.success(request, "Inicio de sesión exitoso.")
                return redirect("dashboard")

        messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "frontend/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not password1 or not password2:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect("register")

        # Crear usuario
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        # Iniciar sesión automáticamente después de registrarse
        login(request, user)
        messages.success(request, "Registro exitoso. ¡Bienvenido!")
        return redirect("dashboard")  # Redirige al Dashboard

    return render(request, "frontend/register.html")


""" def logout_view(request):
    logout(request)
    return redirect('home') """


def logout_view(request):
    request.session.flush()  # Elimina la sesión
    return redirect('home')
