from django import forms
from .models import Reward

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['nome', 'descricao', 'valor_em_creditos', 'imagem']  # Adjust fields as needed