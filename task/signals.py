from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Person

User = get_user_model()


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    # print('AAA')
    if created:
        instance.person = Person.objects.create(user=instance)
    instance.person.save()


# @receiver(pre_delete, sender=User)
# def create_person(sender, instance, created, **kwargs):
#     print('BBB')
#     if created:
#         Person.objects.filter(user=instance).delete()
