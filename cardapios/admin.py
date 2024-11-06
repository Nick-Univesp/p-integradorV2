from django.contrib import admin
from .models import Cardapio, Segmento, Item, Restaurante, CardapioLink
import nested_admin

class ItemInLine(nested_admin.NestedTabularInline):
    model = Item
    extra = 0
    
class SegmentoInline(nested_admin.NestedTabularInline):
    model = Segmento
    extra = 0
    inlines = [ItemInLine]
    
class CardapioCreate(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {"fields": ["nome"]}),
    ]
    inlines = [SegmentoInline]
    
class LinkInline(admin.TabularInline):
    model = CardapioLink
    verbose_name = "Link"
    verbose_name_plural = "Links"
    extra = 0
    
class RestauranteCreate(admin.ModelAdmin):
    inlines = [LinkInline]
    
admin.site.register(Cardapio, CardapioCreate)
admin.site.register(Restaurante, RestauranteCreate)
