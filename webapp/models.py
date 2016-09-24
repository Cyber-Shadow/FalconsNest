from __future__ import unicode_literals
from django.db import models


class ordermodel(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(default = 0.00)
    value = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.name


class menumodel(models.Model):
    categorychoice = (
        ('u','Unorderable'),
        ('sn','Snacks'),
        ('d','Drinks'),
        ('s','Sweets and Desserts'),
        ('i','Icecreams and Iceblocks'),
    )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=14, choices=categorychoice)
    price = models.FloatField(default = 0.00)
    
    def __unicode__(self):
        return self.name
  
        
class usersetting(models.Model):
    name = models.CharField(max_length=50)
    fave = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name

class student(models.Model):
    student_number = models.CharField(max_length=9)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    signedup = models.BooleanField(default=False)
    
    def __unicode__(self):
        return str(self.student_number)
        
    def First_Name(self):
        return self.first_name
    
    def Last_Name(self):
        return self.surname
        
    def Signed_Up(self):
        return self.signedup
