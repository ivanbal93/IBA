from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'slug',
        'get_html_photo'
    )
    search_fields = (
        'id',
        'name',
        'category'
    )
    ordering = ('id', )
    prepopulated_fields = {
        'slug': ('name', )
    }

    # @staticmethod
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_html_photo.short_description = 'photo'