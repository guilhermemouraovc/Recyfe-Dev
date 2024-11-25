from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from ecommerce.produto.models import Variacao
from .models import Pedido, ItemPedido
from ecommerce.utils import utils
import json
from django.conf import settings
import os


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')
        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs

class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Você precisa fazer login.')
            return redirect('register')

        carrinho = self.request.session.get('carrinho')
        if not carrinho:
            messages.error(self.request, 'Seu carrinho está vazio.')
            return redirect('produto:lista')

        carrinho_variacao_ids = [v for v in carrinho]
        bd_variacoes = list(
            Variacao.objects.select_related('produto')
            .filter(id__in=carrinho_variacao_ids)
        )

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
                    'Estoque insuficiente para alguns produtos. Quantidades ajustadas.'
                )
                self.request.session.save()
                return redirect('produto:carrinho')

        qtd_total_carrinho = utils.cart_total_qtd(carrinho)
        valor_total_carrinho = utils.cart_totals(carrinho)

        pedido = Pedido(
            usuario=self.request.user,
            total=valor_total_carrinho,
            qtd_total=qtd_total_carrinho,
            status='C',
        )
        pedido.save()

        itens_pedido = []
        for v in carrinho.values():
            item_pedido = ItemPedido(
                pedido=pedido,
                produto=v['produto_nome'],
                produto_id=v['produto_id'],
                variacao=v['variacao_nome'],
                variacao_id=v['variacao_id'],
                preco=v['preco_quantitativo'],
                preco_promocional=v['preco_quantitativo_promocional'],
                quantidade=v['quantidade'],
                imagem=v['imagem'],
            )
            itens_pedido.append(item_pedido)

        ItemPedido.objects.bulk_create(itens_pedido)

        # Obter o domínio do site atual
        current_site = get_current_site(self.request)
        domain = current_site.domain
        protocol = 'https' if self.request.is_secure() else 'http'
        
        # Preparar itens para o email com URLs absolutas
        itens_email = []
        for item in itens_pedido:
            imagem_url = item.imagem  # URL atual ou caminho da imagem

            item_dict = {
                'produto': item.produto,
                'variacao': item.variacao,
                'quantidade': item.quantidade,
                'total': item.preco_promocional if item.preco_promocional else item.preco,
                'imagem_url': imagem_url,  # URL absoluta da imagem
            }
            itens_email.append(item_dict)

        contexto_email = {
            'pedido': pedido,
            'itens': itens_email,
        }

        mensagem_html = render_to_string(
            'parciais/_email.html',
            contexto_email
        )

        send_mail(
            subject=f'Confirmação do Pedido #{pedido.id}',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.request.user.email],
            fail_silently=False,
            html_message=mensagem_html
        )

        del self.request.session['carrinho']
        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={'pk': pedido.pk}
            )
        )

class Pagar(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'

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