from django.http import JsonResponse
from rest_framework.views import APIView

import services.user

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
