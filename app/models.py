from django.db import models

# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=100)
    bauthor=models.CharField(max_length=100)
    bcost=models.IntegerField()

    def __str__(self):
        return self.bname
