from django.db import models

# Create your models here.
class Metric(models.Model):
    name = models.CharField(max_length=100)

class Quantity(models.Model):
    ammount = models.DecimalField(decimal_places=4, max_digits=20)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(IngredientQuantity)

class Product(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(IngredientQuantity)


