from datetime import datetime

from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, default='name')
    description = models.TextField(default='')
    creation_date = models.DateField(default=datetime.date.today, blank=True)
    user_id = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)
    place = models.TextField(default='')
    photo = models.CharField(default='')
    category_id=models.IntegerField(defaul=1)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
