from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, SiteUser

@receiver(post_save, sender=User )
def create_site_user(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        new_siteuser = SiteUser.objects.create(steamUser=instance)
        instance.siteuser = new_siteuser
        instance.siteuser.save()

# @receiver(post_save, sender=User )
# def save_site_user(sender, instance, **kwargs):
#     instance.siteuser.save()