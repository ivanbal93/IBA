# Generated by Django 4.2.5 on 2023-11-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название коктейля', max_length=50)),
                ('compound', models.TextField(default='Состав коктейля')),
                ('recipe', models.TextField(default='Рецепт приготовления коктейля')),
                ('photo', models.ImageField(upload_to='cocktail_photo/')),
                ('category', models.CharField(choices=[('Незабываемые', 'Незабываемые'), ('Современная классика', 'Современная классика'), ('Напитки новой эры', 'Напитки новой эры')], default='Незабываемые', max_length=30)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
        ),
    ]
