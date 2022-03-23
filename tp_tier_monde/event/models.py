from django.db import models
import datetime
from django.utils import timezone
from django.forms import NumberInput

# Create your models here.

class Users(models.Model):
    name_user = models.CharField(max_length=50)
    firstname_user = models.CharField(max_length=50)
    mail_user = models.CharField(max_length=50)
    pwd_user = models.CharField(max_length=50)

    def __str__(self):
        affiche = f'{name_user},{firstname_user}'
        return affiche

class EventType(models.Model):
    name_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name_type

class HallCategory(models.Model):
    hall_category = models.CharField(max_length=50)

    def __str__(self):
        return self.hall_category

class Material(models.Model):
    category_material = models.CharField(max_length=50)

    def __str__(self):
        return self.category_material

class Artist(models.Model):
    name_artist = models.CharField(max_length=50)
    skill_artist = models.CharField(max_length=50)

    def __str__(self):
        return self.name_artist

class Groups(models.Model):
    name_group = models.CharField(max_length=50)
    type_group = models.CharField(max_length=50)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        affiche = f'{name_group},{type_group}'
        return affiche

class Events(models.Model):
    name_event = models.CharField(max_length=50)
    av_ticket = models.IntegerField(NumberInput)
    begin_date = models.DateTimeField("Date de début d'event")
    end_date = models.DateTimeField("Date de fin d'event")
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    group = models.ManyToManyField(Groups,blank=True)
    user = models.ManyToManyField(Users,blank=True)

    def __str__(self):
        affiche = f'{name_event},{av_ticket},{begin_date},{end_date}'
        return affiche

class Halls(models.Model):
    name_hall = models.CharField(max_length=50)
    size_hall = models.IntegerField(NumberInput)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    hall_category = models.ManyToManyField(HallCategory,blank=True)

    def __str__(self):
        affiche = f'{name_hall},{size_hall},{hall_category}'
        return affiche