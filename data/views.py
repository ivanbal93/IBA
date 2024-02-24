from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

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

    def get_queryset(self):
        '''
        ф-я переопределена для работы поиска
        '''
        query = self.request.GET.get('searching_data')
        if query == None:
            return Cocktail.objects.all().order_by('name')
        return Cocktail.objects.filter(
            Q(name__icontains=query) |
            Q(compound__icontains = query)
        )


class CocktailDetail(DetailView):
    model = Cocktail
    template_name = 'cocktail/cocktail_detail.html'
    context_object_name = 'cocktail'
    slug_url_kwarg = 'cocktail_slug'
