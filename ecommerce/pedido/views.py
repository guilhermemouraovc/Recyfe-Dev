from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages

from ecommerce.produto.models import Variacao
from .models import Pedido, ItemPedido
from ecommerce.utils import utils
from network.models import User
from .models import models

usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")

class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')
        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class Pagar(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'


class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('register')

        # Verificar se o carrinho está na sessão
        carrinho = self.request.session.get('carrinho')
        if not carrinho:
            messages.error(
                self.request,
                'Seu carrinho está vazio.'
            )
            return redirect('produto:lista')

        # Obter as variações do carrinho
        carrinho_variacao_ids = [v for v in carrinho]
        bd_variacoes = list(
            Variacao.objects.select_related('produto')
            .filter(id__in=carrinho_variacao_ids)
        )

        # Verificar o estoque
        for variacao in bd_variacoes:
            vid = str(variacao.id)
            estoque = variacao.estoque
            qtd_carrinho = carrinho[vid]['quantidade']
            preco_unt = carrinho[vid]['preco_unitario']
            preco_unt_promo = carrinho[vid]['preco_unitario_promocional']

            if estoque < qtd_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco_unt
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * preco_unt_promo

                messages.error(
                    self.request,
                    'Estoque insuficiente para alguns produtos do seu carrinho. '
                    'Reduzimos a quantidade desses produtos. Por favor, verifique.'
                )

                self.request.session.save()
                return redirect('produto:carrinho')

        # Calcular o total e a quantidade do carrinho
        qtd_total_carrinho = utils.cart_total_qtd(carrinho)
        valor_total_carrinho = utils.cart_totals(carrinho)

        # Criar o pedido e associá-lo ao usuário
        pedido = Pedido(
            usuario=self.request.user,
            total=valor_total_carrinho,
            qtd_total=qtd_total_carrinho,
            status='C',
        )
        pedido.save()

        # Criar os itens do pedido em massa
        ItemPedido.objects.bulk_create([
            ItemPedido(
                pedido=pedido,
                produto=v['produto_nome'],
                produto_id=v['produto_id'],
                variacao=v['variacao_nome'],
                variacao_id=v['variacao_id'],
                preco=v['preco_quantitativo'],
                preco_promocional=v['preco_quantitativo_promocional'],
                quantidade=v['quantidade'],
                imagem=v['imagem'],
            ) for v in carrinho.values()
        ])

        # Limpar o carrinho
        del self.request.session['carrinho']

        # Redirecionar para a página de pagamento
        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={'pk': pedido.pk}
            )
        )


class Detalhe(DispatchLoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'


class Lista(DispatchLoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'
    template_name = 'pedido/lista.html'
    paginate_by = 10
    ordering = ['-id']
