from django.db import models

# Create your models here.


class Cocktail(models.Model):
    name = models.CharField(
        max_length=50,
        default='Название коктейля',
        null=False
    )
    compound = models.TextField(
        default='Состав коктейля',
        null=False
    )
    recipe = models.TextField(
        default='Рецепт приготовления коктейля',
        null=False
    )
    photo = models.ImageField(
        null=False,
        upload_to=f'cocktail_photo/'
    )
    category = models.CharField(
        choices=(
            ('Незабываемые', 'Незабываемые'),
            ('Современная классика', 'Современная классика'),
            ('Напитки новой эры', 'Напитки новой эры'),
        ),
        max_length=30,
        null=False,
        default='Незабываемые'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL',
        null=True
    )

    def __str__(self):
        return f'id: {self.id}, Название: {self.name}, Категория: {self.category}'
