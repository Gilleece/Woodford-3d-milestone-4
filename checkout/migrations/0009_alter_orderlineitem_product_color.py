# Generated by Django 3.2.1 on 2021-05-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0008_auto_20210523_1526"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderlineitem",
            name="product_color",
            field=models.CharField(blank=True, default="", max_length=10),
        ),
    ]
