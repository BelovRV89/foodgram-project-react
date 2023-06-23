# Generated by Django 3.2.19 on 2023-06-23 12:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='recipes/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='recipes.Ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='recipes.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.ingredient', verbose_name='Ингредиент'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.recipe', verbose_name='Рецепт'),
        ),
    ]
