from datetime import datetime

from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, default='name')
    description = models.TextField(default='')
    creation_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)
    place = models.TextField(default='', max_length=50)
    photo = models.CharField(default='', max_length=50)
    category_id=models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

