# Generated by Django 4.2.4 on 2024-11-09 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedido', '0004_alter_itempedido_id_alter_pedido_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL),
        ),
    ]
