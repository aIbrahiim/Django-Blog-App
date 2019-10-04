from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#function that runs everytime a user is created, post_save is the signal
#when a user is saved send a signal and this signal is going to be received by this receiver and this receiver is this function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #instance is instance of the user
    if created:
        #if the user created create a profile object with the user equals of the instance of the user that was created
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#then import signals in accounts app
