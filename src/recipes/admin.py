from django.contrib import admin

from .models import Recipe, Category


@admin.register(Recipe)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Category)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
