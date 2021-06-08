from django.db import models

# Create your models here.


class Ingredients(models.Model):
    quantity_unit_choices = [
        ("Kgs", "kilograms"),
        ("Lts", "litres"),
        ("Pcs", "pieces"),
    ]

    item_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    quantity = models.PositiveIntegerField(null=False, default=1)
    quantity_unit = models.CharField(max_length=3, choices=quantity_unit_choices, default="Pcs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


class Menu(models.Model):
    dish_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    ingredients = models.ManyToManyField(Ingredients)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dish_name
