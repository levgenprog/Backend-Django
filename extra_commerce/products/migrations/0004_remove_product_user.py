# Generated by Django 4.1.5 on 2023-02-16 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="user",
        ),
    ]
