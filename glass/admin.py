from django.contrib import admin
from .models import Car, Company, Glass, Model
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']


@admin.register(Glass)
class GlassAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car', 'model', 'description', 'price']
