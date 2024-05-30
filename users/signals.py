from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )
        profile.save()


@receiver(post_delete)
def deleteUserProfile(sender, instance, **kwargs):
    user=instance.user
    user.delete()
