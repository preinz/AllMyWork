from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Send(models.Model):
        Email = models.CharField(max_length=30)
        Contact = models.IntegerField(null=True)
        Message = models.TextField(max_length=30, null=True)


        def __str__(self):
            return f'{self.Email}'

class Table(models.Model):
            Denomination_Sociale = models.CharField(max_length=30)
            Type_installation = models.IntegerField(null=True)
            Localisation = models.TextField(max_length=30, null=True)
            Adresse = models.CharField(max_length=30)
            Date_inspection = models.IntegerField(null=True)
            Inspecteurs = models.TextField(max_length=30, null=True)
            Administration = models.CharField(max_length=30)


            def __str__(self):
                return f'{self.Denomination_Sociale}'