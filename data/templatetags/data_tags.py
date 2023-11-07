from django import template
from data.models import *

register = template.Library()

@register.simple_tag
def unforgettable():
    return Cocktail.objects.filter(category='Незабываемые').order_by('name')

@register.simple_tag
def modern_classic():
    return Cocktail.objects.filter(category='Современная классика').order_by('name')

@register.simple_tag
def new_era_drinks():
    return Cocktail.objects.filter(category='Напитки новой эры').order_by('name')
