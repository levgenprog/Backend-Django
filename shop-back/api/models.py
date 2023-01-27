from django.db import models

class Category(models.Model):
    cat_name = models.CharField('name of category', max_length=200)

class Merch(models.Model):
    name = models.CharField('merch name', max_length=200)
    price = models.FloatField('price')
    description = models.TextField('description')
    quantity = models.IntegerField("quantity")
    is_active = models.BooleanField("active")




