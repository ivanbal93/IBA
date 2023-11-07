from django.urls import path

from .views import *


urlpatterns = [
    path('', CocktailsList.as_view(), name='home'),
    path('unforgettable', unforgettable, name='unforgettable'),
    path('modern_classic', modern_classic, name='modern_classic'),
    path('new_era_drinks', new_era_drinks, name='new_era_drinks'),
    path('<slug:cocktail_slug>', CocktailDetail.as_view()),
]
