from django.contrib import admin
from .models import Cliente, Pedido

def formato_clp(valor):
    return f"${valor:,.0f}".replace(",", ".")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'credito_formateado')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'email',)
    def credito_formateado(self, obj):
        return formato_clp(obj.credito_disponible)

    credito_formateado.short_description = 'Crédito Disponible'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'descripcion', 'total_formateado')
    list_filter = ('fecha', 'cliente',)
    search_fields = ('descripcion', 'cliente__nombre',)

    def total_formateado(self, obj):
        return formato_clp(obj.total)

    total_formateado.short_description = 'Total'