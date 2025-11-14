from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Usuário precisa de um username")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    is_template_user = models.BooleanField(default=False)
    objects = CustomUserManager()


class Chamado(models.Model):

    class Prioridade(models.IntegerChoices):
        BAIXA = 1, "Baixa"
        MEDIA = 2, "Média"
        ALTA = 3, "Alta"
        URGENTE = 4, "Urgente"

    class Status(models.TextChoices):
        ABERTO = "ABERTO", "Aberto"
        ATENDIMENTO = "ATENDIMENTO", "Em Atendimento"
        RESOLVIDO = "RESOLVIDO", "Resolvido"
        CANCELADO = "CANCELADO", "Cancelado"

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True)

    prioridade = models.IntegerField(choices=Prioridade.choices, default=Prioridade.MEDIA)
    setor = models.CharField(max_length=100, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ABERTO,
    )

    user_criacao = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    data_criacao = models.DateTimeField(auto_now_add=True)


