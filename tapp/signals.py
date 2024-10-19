from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task

@receiver(post_save, sender=Task)
def set_avator(sender, instance, created, **kwargs):
    if created and not instance.avator:
        instance.avator = 'user.png'
        instance.save()