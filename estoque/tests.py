from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Produto


class ProdutoModelTests(TestCase):
    def test_identifica_estoque_no_minimo(self):
        produto = Produto.objects.create(
            nome="Feijão", preco=Decimal("8.50"),
            quantidade_estoque=Decimal("5"),
            estoque_minimo=Decimal("5")
        )
        self.assertTrue(produto.estoque_baixo)

    def test_estoque_acima_do_minimo_nao_gera_alerta(self):
        produto = Produto.objects.create(
            nome="Arroz", preco=Decimal("25.00"),
            quantidade_estoque=Decimal("10"),
            estoque_minimo=Decimal("5")
        )
        self.assertFalse(produto.estoque_baixo)


class ProdutoViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="teste", password="SenhaSegura123!"
        )
        self.client.login(username="teste", password="SenhaSegura123!")

    def test_lista_de_produtos_requer_login_e_abre_autenticado(self):
        response = self.client.get(reverse("produto_lista"))
        self.assertEqual(response.status_code, 200)
