from django.db import models

# Create your models here.
# class student(models.Model):
#     name=models.CharField(max_length=200)
#     phonenumber=models.IntegerField()
# def str__(self):
#     return self.name
class imageuplaoad(models.Model):
    image=models.ImageField(upload_to='images/')