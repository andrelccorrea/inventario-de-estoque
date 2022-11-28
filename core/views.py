from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from core.models import ConfiguracoesGerais


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["configuracoes"] = ConfiguracoesGerais.load()
