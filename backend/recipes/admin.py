from django.contrib import admin

from . import models


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    list_filter = ('name', 'color')
    search_fields = ('name', 'color')


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'count_favorites')
    list_filter = ('name', 'author', 'tags')
    readonly_fields = ('count_favorites',)
    empty_value_display = '-пусто-'

    def count_favorites(self, obj):
        return obj.favorite_recipe.count()
    count_favorites.short_description = 'Количество добавлений в избранное'


@admin.register(models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'recipe', 'ingredient', 'amount')
    list_filter = ('recipe', 'ingredient')
    search_fields = ('recipe', 'ingredient')

    @staticmethod
    def added_to_favorite(obj):
        return obj.favorite.count()


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')


@admin.register(models.ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')
