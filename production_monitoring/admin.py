from django.contrib import admin
from .models import ProductionCount, MissingDetails

@admin.register(ProductionCount)
class ProductionCountAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'production')
    list_filter = ('date', 'time')
    search_fields = ('date', 'time')

@admin.register(MissingDetails)
class MissingDetailsAdmin(admin.ModelAdmin):
    list_display = ('production_count', 'description', 'missing_date')
    list_filter = ('missing_date',)
    search_fields = ('production_count__date', 'description')

