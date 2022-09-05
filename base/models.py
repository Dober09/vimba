from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class MissingPerson(models.Model):
    SEX_TYPE = (
        ('Male','Male'),
        ('Female','Female')
    )
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    missing_circumstances = models.TextField(null=True ,blank=True)
    gender = models.CharField(max_length=20,choices=SEX_TYPE)
    Police_station = models.CharField(max_length=200)
    station_number = models.CharField(max_length=12)
    e_mail = models.CharField(max_length=200)
    missing_date = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.firstname

class WantedPerson(models.Model):
    SEX_TYPE = (
        ('Male','Male'),
        ('Female','Female')
    )
    # missing_person_image=
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    tags= models.ManyToManyField('Tag',blank=True)
    aliases= models.CharField(max_length=200,default='unknown')
    crime_circumstances = models.TextField(null=True ,blank=True)
    gender = models.CharField(max_length=20,choices=SEX_TYPE)
    Police_station = models.CharField(max_length=200)
    station_number = models.CharField(max_length=12)
    e_mail = models.CharField(max_length=200)
    crime_date = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.firstname

class Tag (models.Model):
    crime = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self) -> str:
        return self.crime
