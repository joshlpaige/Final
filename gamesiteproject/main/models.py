from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):
    
    name = models.CharField(max_length=100)
    about = models.TextField()
    abouttxt = models.TextField(default='')
    facebook = models.CharField(default = '-', max_length=100)
    twitter = models.CharField(default = '-', max_length=100)
    steam = models.CharField(default = '-', max_length=100)
    instagram = models.CharField(default = '-', max_length=100)
    youtube = models.CharField(default = '-', max_length=100)
    git = models.CharField(default = '-', max_length=100)
    linkedin = models.CharField(default = '-', max_length=100)
   
    
    set_name = models.CharField(default = '-', max_length=50)

    picurl = models.TextField(default='')
    picname = models.TextField(default='')

    picurl2 = models.TextField(default='')
    picname2 = models.TextField(default='')


    def __str__(self):
        return self.set_name + " | " + str(self.pk)