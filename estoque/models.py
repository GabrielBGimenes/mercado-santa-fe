from django.core.validators import MinValueValidator
from django.db import models


class Produto(models.Model):
    nome = models.CharField("Nome", max_length=150)
    codigo = models.CharField("Código", max_length=50, unique=True, null=True, blank=True)
    preco = models.DecimalField(
        "Preço", max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantidade_estoque = models.DecimalField(
        "Quantidade em estoque", max_digits=10, decimal_places=3,
        default=0, validators=[MinValueValidator(0)]
    )
    estoque_minimo = models.DecimalField(
        "Estoque mínimo", max_digits=10, decimal_places=3,
        default=0, validators=[MinValueValidator(0)]
    )
    ativo = models.BooleanField("Ativo", default=True)
    data_cadastro = models.DateTimeField("Data de cadastro", auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome

    @property
    def estoque_baixo(self):
        return self.quantidade_estoque <= self.estoque_minimo
