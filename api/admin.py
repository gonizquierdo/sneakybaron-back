from django.contrib import admin
from .models import Summoner

# Register your models here.

@admin.register(Summoner)
class SummonerAdmin(admin.ModelAdmin):
    def url_pretty(self, obj):
        return 'https://api.sneakybaron.gg/api/widget/{}'.format(obj.url)
    fields=('summoner_name', 'region_value')
    list_display=('summoner_name', 'url_pretty')