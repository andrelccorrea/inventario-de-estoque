from django.db import models


class Categoria(models.Model):

    nome = models.CharField(verbose_name="categoria", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self) -> str:
        return self.nome


class Marca(models.Model):

    nome = models.CharField(verbose_name="marca", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"

    def __str__(self) -> str:
        return self.nome


class Pais(models.Model):

    nome = models.CharField(verbose_name="país de origem", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"

    def __str__(self) -> str:
        return self.nome


class TipoVariacao(models.Model):

    nome = models.CharField(verbose_name="tipo de variação", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "tipo de variação"
        verbose_name_plural = "tipos de variações"

    def __str__(self) -> str:
        return self.nome


class Variacao(models.Model):

    tipo_variacao = models.ForeignKey(
        TipoVariacao,
        verbose_name="tipo de variação",
        related_name="conteudos",
        on_delete=models.PROTECT,
    )

    nome = models.CharField(verbose_name="variação", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "variação"
        verbose_name_plural = "variações"

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    class Estacao(models.TextChoices):
        PRIMAVERA = "primavera", "Primavera"
        VERAO = "verao", "Verão"
        OUTONO = "outono", "Outono"
        INVERNO = "inverno", "Inverno"

    categoria = models.ManyToManyField(
        Categoria,
        verbose_name="categoria",
        related_name="produtos",
    )

    marca = models.ForeignKey(
        Marca,
        verbose_name="marca",
        related_name="produtos",
        on_delete=models.PROTECT,
    )

    pais = models.ForeignKey(
        Pais,
        verbose_name="país",
        related_name="produtos",
        on_delete=models.PROTECT,
    )

    descricao = models.TextField(verbose_name="descrição", blank=False, null=False)
    estacao = models.CharField(verbose_name="estação", choices=Estacao.choices, max_length=10)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self) -> str:
        return self.descricao


class Grade(models.Model):

    produto = models.ForeignKey(
        Produto,
        verbose_name="produto",
        related_name="grade",
        on_delete=models.PROTECT,
    )
    variacoes = models.ManyToManyField(
        Variacao,
        verbose_name="variações",
        related_name="grade",
    )
    saldo = models.PositiveIntegerField(verbose_name="saldo", blank=True, null=True, default=0)
    custo = models.FloatField(verbose_name="valor de custo", blank=True, null=True, default=0)
    valor = models.FloatField(verbose_name="valor de venda", default=0)
    lucro = models.FloatField(verbose_name="taxa de lucro", default=0)
    desconto = models.FloatField(verbose_name="taxa de desconto", default=0)
    sku = models.CharField(verbose_name="sku", max_length=255, blank=True, null=True, unique=True)
    gtin = models.CharField(verbose_name="gtin", max_length=255, blank=True, null=True)
