from django.db import models
from django.forms import CharField, IntegerField, NumberInput

# Create your models here.

class Users(models.Model):
    name_user = models.CharField(max_length=50)
    firstname_user = models.CharField(max_length=50)
    mail_user = models.CharField(max_length=50)
    pwd_user = models.CharField(max_length=50)

class EventType(models.Model):
    name_type = models.CharField(max_length=50)

class HallCategory(models.Model):
    hall_category = models.CharField(max_length=50)

class Material(models.Model):
    category_material = models.CharField(max_length=50)

class Artist(models.Model):
    name_artist = models.CharField(max_length=50)
    skill_artist = models.CharField(max_length=50)

class Groups(models.Model):
    name_group = models.CharField(max_length=50)
    type_group = models.CharField(max_length=50)
    artist = models.ManyToManyField(Artist)

class Events(models.Model):
    name_event = models.CharField(max_length=50)
    av_ticket = models.IntegerField(NumberInput)
    begin_date = models.DateTimeField("Date de début d'event")
    end_date = models.DateTimeField("Date de fin d'event")
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    group = models.ManyToManyField(Groups,blank=True)
    user = models.ManyToManyField(Users,blank=True)

class Halls(models.Model):
    name_hall = models.CharField(max_length=50)
    size_hall = models.IntegerField(NumberInput)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    hall_category = models.ManyToManyField(HallCategory,blank=True)
