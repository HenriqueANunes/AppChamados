from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView

import services.user
import services.chamados

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
        return render(request, "user_cadastro.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        status, user_id, descricao = services.user.UserService().cadastrar(email, password, is_template_user=True)

        if status:
            messages.success(request, descricao)
            return redirect("login")

        return render(request, "user_cadastro.html", {"error": descricao})

class ChamadoHomeView(LoginRequiredMixin, View):

    def get(self, request):

        status, lista_chamados, descricao = services.chamados.Chamado().get_chamados()

        return render(request, "home.html", {'lista_chamados': lista_chamados})

class ChamadoCadastroView(LoginRequiredMixin, View):

    def post(self, request, chamado_id=None):

        status, chamado_id, erro = services.chamados.Chamado(request.user).salvar_chamado(
            chamado_id=chamado_id,
            titulo=request.POST.get("titulo"),
            descricao = request.POST.get("descricao"),
            prioridade = request.POST.get("prioridade"),
            setor = request.POST.get("setor"),
        )

        if status:
            return redirect("home")

        messages.error(request, erro)
        return redirect("home")


class VueLoginView(LoginRequiredMixin, TemplateView):
    template_name = "vue/login.html"

class VueHomeView(LoginRequiredMixin, TemplateView):
    template_name = "vue/home.html"

class VueCadastroView(LoginRequiredMixin, TemplateView):
    template_name = "vue/cadastro.html"
