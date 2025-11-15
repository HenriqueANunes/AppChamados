from django.http import JsonResponse
from rest_framework.views import APIView

import services.user
import services.chamados

# Create your views here.
class LoginCadastroView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        status, user_id, descricao = services.user.UserService().cadastrar(email, password, is_template_user=False)

        response = {
            'user_id': user_id,
            'descricao': descricao,
        }

        return JsonResponse(response, status=200 if status else 400)

class ChamadosView(APIView):

    def get(self, request):

        status, lista_chamados, descricao = services.chamados.Chamado().get_chamados(is_tamplate=False)

        response = {
            'lista_chamados': lista_chamados,
        }

        return JsonResponse(response, status=200)

    def patch(self, request, chamado_id):

        status_novo = request.data.get("status")

        status, descricao = services.chamados.Chamado().alterar_status(chamado_id, status_novo)

        return JsonResponse({}, status=200 if status else 400)
