from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import api.views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("login/cadastro", api.views.LoginCadastroView.as_view(), name="login_cadastro"),
]
