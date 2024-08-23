from django.dispatch import receiver
from django.db.models.signals import (pre_save, post_save)
from tapp.models import Author


@receiver(pre_save, sender=Author)
def test_pre_signal(sender, *args, **kwargs):
    """
    Before author is added to our database
    """
    print(f'Pre-Save: Author created')


@receiver(post_save, sender=Author)
def test_post_signal(sender, instance, created, *args, **kwargs):
    """
    After author is added to our database
    """
    if created:
        id = instance.id
        Author.objects.filter(id=id).update(name=f'Author {instance.name}')
    else:
        print(f'Error creating author')