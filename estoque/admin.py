from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "preco", "quantidade_estoque", "estoque_minimo", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome", "codigo")
