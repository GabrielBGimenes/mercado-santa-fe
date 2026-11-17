from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProdutoForm
from .models import Produto


@login_required
def produto_lista(request):
    termo = request.GET.get("q", "").strip()
    produtos = Produto.objects.all()
    if termo:
        produtos = produtos.filter(nome__icontains=termo) | produtos.filter(codigo__icontains=termo)
    return render(request, "estoque/produto_lista.html", {
        "produtos": produtos.distinct(),
        "termo": termo,
    })


@login_required
def produto_criar(request):
    form = ProdutoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produto_lista")
    return render(request, "estoque/produto_form.html", {"form": form, "titulo": "Cadastrar produto"})


@login_required
def produto_editar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produto_lista")
    return render(request, "estoque/produto_form.html", {"form": form, "titulo": "Editar produto"})
