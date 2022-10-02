from django.db import models


class Categoria(models.Model):

    nome = models.CharField(verbose_name="categoria", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"


class SubCategoria(models.Model):

    nome = models.CharField(verbose_name="subcategoria", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "subcategoria"
        verbose_name_plural = "subcategorias"


class CategoriaTerceiroNivel(models.Model):

    nome = models.CharField(
        verbose_name="categoria de terceiro nível", max_length=255, blank=False, null=False, unique=True
    )

    class Meta:
        verbose_name = "categoria de terceiro nível"
        verbose_name_plural = "categorias de terceiro nível"


class Marca(models.Model):

    nome = models.CharField(verbose_name="marca", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"


class Material(models.Model):

    nome = models.CharField(verbose_name="material", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materiais"


class Pais(models.Model):

    nome = models.CharField(verbose_name="país de origem", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"


class Estampa(models.Model):

    nome = models.CharField(verbose_name="tipo de estampa", max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "estampa"
        verbose_name_plural = "estampas"


# class Variacao(models.Model):
#     # fk do produto, gtin, sku, saldo, preço, nome (cor, tamanho),
#     # possibilidades (p,m,g / branco, amarelo, vermelho )
#     pass


class Produto(models.Model):
    class Estacao(models.TextChoices):
        PRIMAVERA = "primavera", "Primavera"
        VERAO = "verao", "Verão"
        OUTONO = "outono", "Outono"
        INVERNO = "inverno", "Inverno"

    categoria = models.ForeignKey(
        Categoria,
        verbose_name="categoria",
        related_name="categorias",
        on_delete=models.PROTECT,
    )
    subcategoria = models.ForeignKey(
        SubCategoria,
        verbose_name="subcategoria",
        related_name="subcategorias",
        on_delete=models.PROTECT,
    )
    categoria3 = models.ForeignKey(
        CategoriaTerceiroNivel,
        verbose_name="categoria de terceiro nível",
        related_name="categorias_3_nivel",
        on_delete=models.PROTECT,
    )
    marca = models.ForeignKey(
        Marca,
        verbose_name="marca",
        related_name="marcas",
        on_delete=models.PROTECT,
    )
    material = models.ForeignKey(
        Material,
        verbose_name="material",
        related_name="materiais",
        on_delete=models.PROTECT,
    )
    pais = models.ForeignKey(
        Pais,
        verbose_name="país",
        related_name="países",
        on_delete=models.PROTECT,
    )
    estampa = models.ForeignKey(
        Estampa,
        verbose_name="estampa",
        related_name="estampas",
        on_delete=models.PROTECT,
    )

    descricao = models.TextField(verbose_name="descrição", blank=False, null=False)
    saldo = models.PositiveIntegerField(verbose_name="saldo", blank=True, null=True, default=0)
    custo = models.FloatField(verbose_name="valor de custo", blank=True, null=True, default=0)
    valor = models.FloatField(verbose_name="valor de venda", default=0)
    lucro = models.FloatField(verbose_name="taxa de lucro", default=0)
    desconto = models.FloatField(verbose_name="taxa de desconto", default=0)

    estacao = models.CharField(verbose_name="estação", choices=Estacao.choices, max_length=10)
    sku = models.CharField(verbose_name="sku", max_length=255, blank=True, null=True, unique=True)
    gtin = models.CharField(verbose_name="gtin", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"
