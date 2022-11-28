from core.models import ConfiguracoesGerais


def configuracoes(request):
    return {"configuracoes": ConfiguracoesGerais.load()}
