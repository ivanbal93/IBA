from rest_framework.serializers import ModelSerializer
from .models import Cocktail


class CocktailSerializer(ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'
