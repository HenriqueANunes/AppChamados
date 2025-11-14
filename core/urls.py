from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import core.views

urlpatterns = [
    path("login/", core.views.LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("cadastro/", core.views.UserCadastroView.as_view(), name="cadastro"),

    path("home/", core.views.HomeView.as_view(), name="home"),

]
