from django.contrib import admin

from .models import (
    Categoria,
    Grade,
    Marca,
    Produto,
    TipoVariacao,
    Variacao,
)

# TODO:
# configurar para executar no docker
# fazer o deploy seguindo o tutorial:
# https://medium.com/codex/run-your-docker-containers-for-free-in-the-cloud-and-for-unlimited-time-361515cb0876#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImJhMDc5YjQyMDI2NDFlNTRhYmNlZDhmYjEzNTRjZTAzOTE5ZmIyOTQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NjQ3MzM0NzgsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExNTAyNzM0Nzk4NDU5MDc4NzEyNyIsImVtYWlsIjoiYW5kcmUubGNjb3JyZWFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiJBbmRyw6kgQ29ycsOqYSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQUNOUEV1X0xIN1RUVUJ0YmdTbnpsWWwyWGE2M1RhS3VHUFlTa3F3MVN3TnpDUT1zOTYtYyIsImdpdmVuX25hbWUiOiJBbmRyw6kiLCJmYW1pbHlfbmFtZSI6IkNvcnLDqmEiLCJpYXQiOjE2NjQ3MzM3NzgsImV4cCI6MTY2NDczNzM3OCwianRpIjoiZjZlNWJjYmZkYzc3OTgwYzgyZjU1ZGQyNzczY2JkMGM4MzM5NGNjNyJ9.OcU7SXJmfP1O265AC4C-h_JndQlYumAlofLLaSgLMOsJHSlz3JiqyvxsnEZXaDsWOLrhMvoHCbSp8qsztNtYIyX_6uiMnkEYGx7D7fGM7KtvpMI-Co2BvrR44OR8Wchs4tmcJmlrnFYVwg7yrMZgU3utDmi6RlCd5AADGehip93YS0NCF8QM841c2MjpyZET8SdUM6Qirn_sXyd_fobqwDO_O-wbmznDxIdKsHZXAn4ZL95eCUgx6z_-yf3t1x3SMU1OhekacZnePr80RwDpC0tW2whuhbuVNZvZfzTsWVKJ0e1gq7ixM9RNnT100PoufKtoFdPQ68BXSR-V_T2GLQ


class CategoriaAdmin(admin.ModelAdmin):
    fields = ("nome",)
    search_fields = ("nome",)


class MarcaAdmin(admin.ModelAdmin):
    fields = ("nome",)
    search_fields = ("nome",)


class VariacaoAdmin(admin.ModelAdmin):
    fields = ("tipo_variacao", "nome")
    list_display = ("nome", "tipo_variacao")
    search_fields = ("nome",)


class TipoVariacaoAdmin(admin.ModelAdmin):
    fields = ("nome",)
    search_fields = ("nome",)


class InlineGradeAdmin(admin.TabularInline):
    model = Grade


class ProdutoAdmin(admin.ModelAdmin):
    fields = (
        "descricao",
        ("categorias", "marca", "estacao"),
    )
    list_display = ("descricao", "get_categorias", "marca", "estacao")
    list_filter = ("categorias", "marca", "descricao", "estacao")
    search_fields = ("categorias__nome", "marca__nome", "descricao", "estacao")

    autocomplete_fields = ("categorias", "marca")

    inlines = (InlineGradeAdmin,)

    @admin.display(description="Categorias")
    def get_categorias(self, obj):
        return "; ".join([categoria.nome for categoria in obj.categorias.all()])


class GradeAdmin(admin.ModelAdmin):
    list_display = ("produto", "get_variacoes", "saldo", "valor")
    list_filter = ("produto__descricao", "variacoes")
    search_fields = ("produto__descricao",)
    autocomplete_fields = ("produto", "variacoes")
    ordering = ("-saldo", "produto__descricao")

    @admin.display(description="Variações")
    def get_variacoes(self, obj):
        return "; ".join([variacao.nome for variacao in obj.variacoes.all()])


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(TipoVariacao, TipoVariacaoAdmin)
admin.site.register(Variacao, VariacaoAdmin)
