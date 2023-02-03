from django.db import models


# Create your models here.
class MyDetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    post=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')


class Skill(models.Model):
    skill_name=models.CharField(max_length=100)

class Project(models.Model):
    image=models.ImageField(upload_to='media')
    link=models.URLField(default='')

class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
   
    message=models.TextField()
  
