from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    telegram_chat_id = models.CharField(max_length=100)
    telegram_username = models.CharField(max_length=100)
    profile_photo = models.CharField(max_length=400)
    faculty = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    year_of_study = models.IntegerField()