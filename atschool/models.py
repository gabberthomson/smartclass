from django.db import models

# Create your models here.

class School(models.Model):
    descr = models.CharField(max_length=100)

class Class(models.Model):
    descr = models.CharField(max_length=100)
    school = models.ForeignKey(School)

class Subject(models.Model):
    descr = models.CharField(max_length=100)
    
