from django.db import models
from django.utils import timezone


class NGUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=(('male', 'мужской'), ('female', 'женский')))
    address = models.CharField(max_length=100)
    email = models.EmailField()
    avatar_url = models.CharField(max_length=200)


class NGMessage(models.Model):
    sender = models.ForeignKey(NGUser, related_name='sender')
    recipient = models.ForeignKey(NGUser, related_name='recipient')
    date_and_time = models.DateTimeField(default=timezone.now)
    text = models.TextField(null=True)
