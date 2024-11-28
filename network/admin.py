from django.contrib import admin, messages

from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follower)
#admin.site.register(Like)
#admin.site.register(Saved)
admin.site.register(MapPoint)
class MapPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'description')
    search_fields = ('name', 'description')

@admin.action(description="Adicionar créditos aos usuários selecionados")
def adicionar_creditos(modeladmin, request, queryset):
    for user_credit in queryset:
        user_credit.saldo += 100  # Adicione 100 créditos (ajuste conforme necessário)
        user_credit.save()
    messages.success(request, "Créditos adicionados com sucesso!")

@admin.register(UserCredits)
class UserCreditsAdmin(admin.ModelAdmin):
    list_display = ('user', 'saldo')
    actions = [adicionar_creditos]