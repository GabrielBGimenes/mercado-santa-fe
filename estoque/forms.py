
from django import forms
from django.core.validators import MinValueValidator
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome", "codigo", "preco",
            "quantidade_estoque", "estoque_minimo", "ativo"
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={
                "class": "form-control", "min": "0", "step": "0.01"
            }),
            "quantidade_estoque": forms.NumberInput(attrs={
                "class": "form-control", "min": "0", "step": "0.001"
            }),
            "estoque_minimo": forms.NumberInput(attrs={
                "class": "form-control", "min": "0", "step": "0.001"
            }),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean_nome(self):
        nome = self.cleaned_data["nome"].strip()

        if not nome:
            raise forms.ValidationError("O nome do produto é obrigatório.")

        return nome

    def clean_preco(self):
        preco = self.cleaned_data["preco"]

        if preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")

        return preco

    def clean_quantidade_estoque(self):
        quantidade = self.cleaned_data["quantidade_estoque"]

        if quantidade < 0:
            raise forms.ValidationError("O estoque não pode ser negativo.")

        return quantidade

    def clean_estoque_minimo(self):
        minimo = self.cleaned_data["estoque_minimo"]

        if minimo < 0:
            raise forms.ValidationError("O estoque mínimo não pode ser negativo.")

        return minimo
