import logging

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Use get_or_create so we don't raise if a profile already exists
        profile, created_flag = UserProfile.objects.get_or_create(user=instance)
        if created_flag:
            logger.info("Created UserProfile for user=%s", instance.username)
