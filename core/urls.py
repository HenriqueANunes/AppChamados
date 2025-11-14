from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import core.views

urlpatterns = [
    path("login/", core.views.LoginView.as_view(), name="login"),
    path("login/cadastro/", core.views.UserCadastroView.as_view(), name="user_cadastro"),

    path("home", core.views.ChamadoHomeView.as_view(), name="home"),
    path("home/chamado", core.views.ChamadoCadastroView.as_view(), name="home_chamado"),
    path("home/chamado/<int:chamado_id>", core.views.ChamadoCadastroView.as_view(), name="home_chamado"),

]
