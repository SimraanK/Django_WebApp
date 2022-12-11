from operator import mod
from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)

    email = models.CharField(max_length=100, null=False, blank=False)

    phone = models.CharField(max_length=15, null=False, blank=False)

    feedback = models.TextField()

    date = models.DateField()


    def __str__(self):
        return self.name