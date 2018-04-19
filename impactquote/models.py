from django.db import models
from taggit.managers import TaggableManager

class Quote(models.Model):
    quote=models.CharField(max_length=300)
    movie=models.CharField(max_length=100,default='text')
    tags=TaggableManager()


    def __str__(self):
        return self.quote



