# Generated by Django 4.1.5 on 2023-02-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="data",
            field=models.JSONField(
                blank=True, default=dict, null=True, verbose_name="Data"
            ),
        ),
    ]