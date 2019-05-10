from django.db import models
from dependencies.models import Dependent
# Create your models here.

class Video (models.Model):
    dependent = models.name = models.ForeignKey(Dependent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    video_link = models.URLField()
    #sports categoryeld
    notes = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dependent.first_name

