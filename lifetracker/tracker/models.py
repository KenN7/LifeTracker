from django.db import models
from django.contrib import auth
#from django.db.models import Sum
from django.core.validators import RegexValidator
#from colorful import fields
from django.utils import timezone
import paho.mqtt.publish as pub

#import datetime


# Create your models here.
class User(auth.models.User):

    class Meta:
        proxy = True

    def actusensors(self):
        return self.actusensor.all()
    #def daily_events(self):
        #today = datetime.datetime.today()
        #return self.events.filter(date__year=today.year, date__month=today.month, date__day=today.day)

    #def tomorrow_events(self):
        #today = datetime.datetime.today()
        #return self.events.filter(date__year=today.year, date__month=today.month, date__day=today.day+1)

    #def later_events(self):
        #today = datetime.datetime.today()
        #return self.events.filter(date__gt=today)


#class Period(models.Model):
    #frequency = models.IntegerField()

    #def __str__(self):
        #return str(self.frequency)


class Pad(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name


#class Events(models.Model):
    #TYPES = (
        #('Notif', 'Notification'),
        #('Event', 'Event'),
    #)
    #name = models.CharField(max_length=50)
    #date = models.DateTimeField()
    #desc = models.TextField()
    #author = models.ForeignKey(User, related_name='events')
    #recurent = models.ForeignKey(Period, related_name='events')
    #icon = models.ForeignKey(Icon, related_name='events')
    #eventtype = models.CharField(max_length=20, choices=TYPES, default='Event')


    #def __str__(self):
        #return self.name


class Todo(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name='todo')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Actusensor(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, related_name='actusensor')
    topic = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    host = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Command(models.Model):
    name = models.CharField(max_length=30)
    command = models.CharField(max_length=50)
    actusensor = models.ForeignKey(Actusensor, related_name='sensor')

    def __str__(self):
        return self.name
    
    def send(self, message):
        pub.single(actusensor.topic, payload=message, hostname=host)

class Data(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=50)
    actusensor = models.ForeignKey(Actusensor, related_name='data')

    def __str__(self):
        return self.name
