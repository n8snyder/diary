from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class PageManager(models.Manager):
    def get_todays_page(self, user):
        start = timezone.now().date()
        end = start + timedelta(1)
        page = Page.objects.filter(
            user=user, date_created__gt=start, date_created__lt=end
        )
        if page:
            return page.first()
        else:
            return Page.objects.create(user=user)


class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    objects = PageManager()

    @property
    def number(self):
        pages = list(Page.objects.filter(user=self.user).order_by("-date_created"))
        number = pages.index(self) + 1
        return number
