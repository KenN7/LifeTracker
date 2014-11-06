from django.db import models
from django.contrib import auth
#from django.db.models import Sum
from django.core.validators import RegexValidator
#from colorful import fields

# Create your models here.
class User(auth.models.User):
    
    class Meta:
        proxy = True

    def bla(self):
        pass


class Period(models.Model):
    frequency = models.IntegerField()

    def __str__(self):
        return self.frequency


class Pad(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Icon(models.Model):
    name = models.CharField(max_length=30)
    path = models.FilePathField()

    def __str__(self):
        return self.name


class Events(models.Model):
    TYPES = (
        ('Notif', 'Notification'),
        ('Event', 'Event'),
    )
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    author = models.ForeignKey(User, related_name='events')
    recurent = models.ForeignKey(Period, related_name='events')
    icon = models.ForeignKey(Icon, related_name='events')
    eventtype = models.CharField(max_length=20, choices=TYPES, default='Event')

    def __str__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name='todo')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


