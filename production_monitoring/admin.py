from django.contrib import admin
from .models import ProductionCount, Machine

@admin.register(ProductionCount)
class ProductionCountAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'production')
    list_filter = ('date', 'time')
    search_fields = ('date', 'time')

# @admin.register(MissingDetails)
# class MissingDetailsAdmin(admin.ModelAdmin):
#     list_display = ('production_count', 'description', 'missing_date')
#     list_filter = ('missing_date',)
#     search_fields = ('production_count__date', 'description')


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ["machineID","name","manufacture","model","line"]
    list_filter = ["machineID","name","manufacture","model","line"]
    search_fields = ["machineID","name","manufacture","model","line"]