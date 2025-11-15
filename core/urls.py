from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import core.views

urlpatterns = [
    path("login/", core.views.LoginView.as_view(), name="login"),
    path("login/cadastro/", core.views.UserCadastroView.as_view(), name="user_cadastro"),

    path("home", core.views.ChamadoHomeView.as_view(), name="home"),
    path("home/chamado", core.views.ChamadoCadastroView.as_view(), name="home_chamado"),
    path("home/chamado/<int:chamado_id>", core.views.ChamadoCadastroView.as_view(), name="home_chamado"),

    path('vue/login', core.views.VueLoginView.as_view(), name='vue_login'),
    path('vue/cadastro', core.views.VueCadastroView.as_view(), name='vue_cadatro'),
    path('vue/home', core.views.VueHomeView.as_view(), name='vue_app'),

]
