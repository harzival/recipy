from django.contrib import admin

# Register your models here.
from .models import Metric, Quantity, Ingredient, Recipe, Product, IngredientQuantity

admin.site.register(Metric)
admin.site.register(Quantity)
admin.site.register(Ingredient)
admin.site.register(IngredientQuantity)
admin.site.register(Recipe)
admin.site.register(Product)