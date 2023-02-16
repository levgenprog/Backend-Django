from django.db import models

class OrderStatusChoices(models.TextChoices):
    New = 'New'
    InProgress = 'InProgress'
    Canceled = 'Canceled'
    Paid = 'Paid'