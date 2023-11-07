from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.


def index(request):
    return render(
        request,
        template_name='data/default.html'
    )


def unforgettable(request):
    return render(
        request,
        template_name='cocktail/unforgettable.html'
    )


def modern_classic(request):
    return render(
        request,
        template_name='cocktail/modern_classic.html'
    )


def new_era_drinks(request):
    return render(
        request,
        template_name='cocktail/new_era_drinks.html'
    )


class CocktailsList(ListView):
    model = Cocktail
    ordering = 'name'
    template_name = 'cocktail/cocktails_list.html'
    context_object_name = 'cocktails_list'


class CocktailDetail(DetailView):
    model = Cocktail
    template_name = 'cocktail/cocktail_detail.html'
    context_object_name = 'cocktail'
    slug_url_kwarg = 'cocktail_slug'
