from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Profile(models.Model):
        Email = models.CharField(max_length=30)
        Message = models.CharField(max_length=30, null=True)
        Contact = models.IntegerField(null=True)
        type = models.ForeignKey(User, related_name='profiles', on_delete=models.CASCADE, null=True)

        def __str__(self):
            return f'{self.name}'