from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=10)
    slocation=models.CharField(max_length=10)
    sprincipal=models.CharField(max_length=10)
    sstrength=models.IntegerField()