from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

import services.user

# Create your views here.
class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.is_template_user:
                return render(
                    request,
                    "login.html",
                    {"error": "Esta conta não pode acessar via templates."}
                )

            login(request, user)
            return redirect("home")

        return render(request, "login.html", {"error": "Credenciais inválidas"})


class UserCadastroView(View):
    def get(self, request):
        return render(request, "cadastro.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        status, user_id, descricao = services.user.UserService().cadastrar(email, password, is_template_user=True)

        if status:
            messages.success(request, descricao)
            return redirect("login")

        return render(request, "cadastro.html", {"error": descricao})

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
    def post(self, request):
        pass
