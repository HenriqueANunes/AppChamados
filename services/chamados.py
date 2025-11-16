import core.models

class Chamado:

    def __init__(self, user_criacao = None):
        self.user_criacao = user_criacao

    def get_chamados(self, is_tamplate=True):

        if is_tamplate:
            lista_chamados = core.models.Chamado.objects.all()
        else:
            lista_chamados = list(core.models.Chamado.objects.values())

        return True, lista_chamados, ''

    def salvar_chamado(self, titulo:str, prioridade:int, chamado_id:int = None, descricao:str = None,
                          setor:str = None):

        if chamado_id:
            try:
                chamado = core.models.Chamado.objects.get(id=chamado_id)
            except core.models.Chamado.DoesNotExist:
                return False, None, 'Chamado não encontrado'

        else:
            chamado = core.models.Chamado()

        chamado.titulo = titulo
        chamado.prioridade = prioridade
        chamado.status = chamado.status or 'ABERTO'
        chamado.descricao = descricao
        chamado.setor = setor
        chamado.user_criacao = self.user_criacao

        chamado.save()

        return True, chamado.id, ''

    def alterar_status(self, chamado_id:int, status:str):

        if not core.models.Chamado.objects.filter(id=chamado_id).exists():
            return False, 'Chamado não encontrado'

        core.models.Chamado.objects.filter(id=chamado_id).update(status=status)

        return True, ''
