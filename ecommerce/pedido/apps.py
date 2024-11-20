from django.apps import AppConfig

class PedidoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce.pedido'  # Caminho completo do app
    verbose_name = 'Pedidos'