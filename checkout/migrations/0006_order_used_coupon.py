# Generated by Django 3.2.1 on 2021-05-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0005_coupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="used_coupon",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
