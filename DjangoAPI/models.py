# Create your models here.
from django.db import models
class Customer(models.Model ):
    GENDER_CHOICES = (('Male','Male'),('Female', 'Female') )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
            return self.gender