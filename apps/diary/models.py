from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    @property
    def number(self):
        pages = list(Page.objects.filter(user=self.user).order_by("-date_created"))
        number = pages.index(self) + 1
        return number
