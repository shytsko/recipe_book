from django.contrib import admin

from .models import Recipe, Сategory


@admin.register(Recipe)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Сategory)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
