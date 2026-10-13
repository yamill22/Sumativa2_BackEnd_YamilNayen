from django.contrib import admin
from .models import editorial, libro


class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    list_filter = ('nombre',)
    search_fields = ('nombre', 'direccion', 'telefono')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'fecha_publicacion', 'precio_pesos')
    list_filter = ('editorial', 'fecha_publicacion')
    search_fields = ('titulo', 'autor', 'editorial__nombre')

    @admin.display(description='Precio', ordering='precio')
    def precio_pesos(self, obj):
        return f"${obj.precio:,}".replace(",", ".")


admin.site.register(editorial, EditorialAdmin)
admin.site.register(libro, LibroAdmin)