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
    avatar_user = models.ImageField(upload_to='avatar', blank=True)

    def __str__(self):
        affiche = f"{self.name_user} {self.firstname_user}"
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
    pics_artist = models.ImageField(upload_to='picsArtist', blank=True)

    def __str__(self):
        affiche = f"{self.name_artist} {self.skill_artist}"
        return affiche


class Groups(models.Model):
    name_group = models.CharField(max_length=50)
    type_group = models.CharField(max_length=50)
    artist = models.ManyToManyField(Artist)
    pics_group = models.ImageField(upload_to='picsArtist', blank=True)

    def __str__(self):
        affiche = f"{self.name_group} {self.type_group}"
        return affiche


class Events(models.Model):
    name_event = models.CharField(max_length=50)
    av_ticket = models.IntegerField(NumberInput, null=True)
    begin_date = models.DateTimeField("Date de dÃ©but d'event")
    end_date = models.DateTimeField("Date de fin d'event")
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    group = models.ManyToManyField(Groups,blank=True)
    user = models.ManyToManyField(Users,blank=True)

    def __str__(self):
        affiche = f" {self.name_event}  {self.av_ticket}"
        return affiche 

class Halls(models.Model):
    name_hall = models.CharField(max_length=50)
    size_hall = models.IntegerField(NumberInput, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    hall_category = models.ManyToManyField(HallCategory,blank=True)

    def __str__(self):
        affiche =f" {self.name_hall} {self.size_hall} {self.hall_category}"
        return affiche
