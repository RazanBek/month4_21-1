from django.contrib import admin
from main.models import Film, Director


class ProductAdmin(admin.ModelAdmin):
    list_display = 'title director regiser rating dlitelnost created updated'.split()
    search_fields = 'title'.split()
    list_filter = 'director regiser rating created updated'.split()
    list_editable = 'director regiser rating'.split()


admin.site.register(Film, ProductAdmin)
admin.site.register(Director)
