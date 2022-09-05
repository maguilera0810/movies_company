from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.core.models import DatedModel


class Person(DatedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_user_person(sender, instance, **kwargs):
    instance.person.save()


class Alias(DatedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)


# data = {"username": "maguilera0810@gmail.com", "first_name": "Mauricio", "last_name": "Aguilera",
#         "email": "maguilera0810@gmail.com", "password": "123456", "is_staff": False, "is_active": True, "is_superuser": False}
# user = User(username=data.get("email"), first_name=data.get("first_name"), last_name=data.get("last_name"), email=data.get("email"), password=data.get(
#     "password"), is_staff=data.get("is_staff", False), is_active=data.get("is_active", True), is_superuser=data.get("is_superuser", False))
