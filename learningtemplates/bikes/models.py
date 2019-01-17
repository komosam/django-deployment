from django.db import models
#from datetime import datetime
from django.utils import timezone
# Create your models here.

class registrations(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    created_date =  models.DateTimeField(default=timezone.now)
