from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserService:

    def __init__(self, user_id: int = None):
        self.user_id = user_id

    def cadastrar(self, email: str, password: str, is_template_user: bool):
        # Verifica se já existe
        if UserModel.objects.filter(username=email).exists():
            return False, None, 'Esse email já está cadastrado'

        user = UserModel.objects.create_user(
            username=email,
            email=email,
            password=password,
            is_template_user=is_template_user,
        )

        return True, user.id, 'Conta criada com sucesso! Faça login para continuar.'
