from django.apps import AppConfig

class ProdutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce.produto'
    verbose_name = 'Produtos'