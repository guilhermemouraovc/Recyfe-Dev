from django.apps import AppConfig

class LojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce.loja'
    verbose_name = 'Loja'

class NetworkConfig(AppConfig):
    name = 'network'
