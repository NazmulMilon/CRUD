from django.db import models


# Create your models here.
class Client(models.Model):
    No = models.IntegerField()
    Name = models.CharField(max_length=64)
    Father_name = models.CharField(max_length=64)
    Mother_name = models.CharField(max_length=64)
    Address = models.CharField(max_length=256)
    Contact = models.IntegerField()
