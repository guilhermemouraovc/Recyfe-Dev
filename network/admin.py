from django.contrib import admin

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