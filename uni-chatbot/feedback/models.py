from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class BaseFeedback(models.Model):
    type = models.CharField(max_length=255, choices=settings.FEEDBACK_CHOICES, verbose_name=_('Type'))
    message = models.TextField(verbose_name=_('Message'))
    time = models.DateTimeField(auto_now_add = True, verbose_name=_('Time'))

    class Meta:
        ordering = ('time',)
        abstract = True

    def _str_(self) -> str:
        return self.message

class Feedback(BaseFeedback):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))

class AnonymousFeedback(BaseFeedback):
    user = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('User'))




