# Generated by Django 4.1.5 on 2023-02-02 15:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, unique=True, verbose_name="Title"),
                ),
                ("body", models.TextField(verbose_name="Body")),
                (
                    "main_image",
                    models.ImageField(
                        upload_to="products/%Y/%m/%d/", verbose_name="Main image"
                    ),
                ),
                ("is_top", models.BooleanField(default=False, verbose_name="Is top")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is active"),
                ),
                ("data", models.JSONField(default=dict, verbose_name="Data")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("is_top", "-created_at"),
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="product-images/%Y/%m/%d/", verbose_name="Image"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="products.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product image",
                "verbose_name_plural": "Products images",
                "ordering": ("-created_at",),
            },
        ),
    ]
