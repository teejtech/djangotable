from django.db import models

"""class Table1(models.Model):
    fname=models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    emp=models.BooleanField(null=False)"""

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    age=models.IntegerField()
    emp=models.BooleanField(null=False)

'''class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()'''

