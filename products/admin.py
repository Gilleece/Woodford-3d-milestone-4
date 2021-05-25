from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "image",
    )

    ordering = ("name",)


admin.site.register(Product, ProductAdmin)
