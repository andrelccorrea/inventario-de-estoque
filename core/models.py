from django.core.cache import cache
from django.db import models


class ConfiguracoesGerais(models.Model):

    # TODO: Adicionar validações para os campos abaixo

    fantasia = models.CharField(verbose_name="fantasia", max_length=255, blank=True, null=True)
    razao_social = models.CharField(verbose_name="razão social", max_length=255, blank=True, null=True)
    cpf = models.CharField(verbose_name="cpf", max_length=11, blank=True, null=True)
    cnpj = models.CharField(verbose_name="cnpj", max_length=14, blank=True, null=True)
    ddd = models.CharField(verbose_name="ddd", max_length=2, blank=True, null=True)
    telefone = models.CharField(verbose_name="telefone", max_length=8, blank=True, null=True)
    celular = models.CharField(verbose_name="celular", max_length=9, blank=True, null=True)
    rua = models.CharField(verbose_name="rua", max_length=255, blank=True, null=True)
    numero = models.CharField(verbose_name="numero", max_length=5, blank=True, null=True)
    bairro = models.CharField(verbose_name="bairro", max_length=255, blank=True, null=True)
    cidade = models.CharField(verbose_name="cidade", max_length=255, blank=True, null=True)
    cep = models.CharField(verbose_name="cep", max_length=8, blank=True, null=True)
    logo = models.ImageField(verbose_name="logo", blank=True, null=True)
    banner = models.ImageField(verbose_name="banner", blank=True, null=True)

    class Meta:
        verbose_name = "configurações"
        verbose_name_plural = "configurações"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

    def set_cache(self):
        cache.set(self.__class__.__name__, self)
