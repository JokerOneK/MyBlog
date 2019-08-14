import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    theme = models.CharField(max_length=100)
    post_text = models.CharField(max_length=4000)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("Blog:detail", kwargs={'pk': self.pk})  # реверс - работает без пк kwargs={'pk': self.pk}

    def __str__(self):
        return self.theme

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.self_description = 'Published recently?'



# Create your models here.
