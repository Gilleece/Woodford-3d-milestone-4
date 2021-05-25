from django.db import models


class Product(models.Model):
    """
    Model for products within the store
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_colors = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default="", blank=True)

    def __str__(self):
        return self.name
