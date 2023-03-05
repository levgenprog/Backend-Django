from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync

from . import models


@receiver(post_save, sender=models.Order)
def send_order_notification(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        str(instance.id),
        {
            'type': 'send_notification',
            'status': instance.status,
        }
    )
