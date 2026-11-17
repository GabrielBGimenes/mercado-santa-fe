from django import forms
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
            "preco": forms.NumberInput(attrs={"class": "form-control", "min": "0", "step": "0.01"}),
            "quantidade_estoque": forms.NumberInput(attrs={"class": "form-control", "min": "0", "step": "0.001"}),
            "estoque_minimo": forms.NumberInput(attrs={"class": "form-control", "min": "0", "step": "0.001"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
