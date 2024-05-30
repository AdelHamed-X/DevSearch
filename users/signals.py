from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name,
            username=user.username,
            email=user.email,
        )
