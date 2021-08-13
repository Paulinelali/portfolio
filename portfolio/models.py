from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Projectmodel(models.Model):
    title = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=250)
    img = models.ImageField(blank=True, upload_to ='uploads/images')
    url = models.URLField(blank=True)
    date_created = models.DateField()
    platform = models.CharField(blank=True, max_length=100)
    
class myInfo(models.Model):
    mypic = models.ImageField(blank=True, upload_to ='uploads/images')
    logo = models.ImageField(blank=True, upload_to ='uploads/images')
    myskills = models.CharField(blank=True, max_length=100)