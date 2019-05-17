from django.db import models
from media_content.models import SportsCategory
from django.conf import settings
User = settings.AUTH_USER_MODEL 
# Create your models here.

class Dependent(models.Model):
    guardian =models.ForeignKey(User,on_delete=models.CASCADE)
    sports_category = models.ForeignKey(SportsCategory,on_delete=models.CASCADE,blank=True, null=True)
    first_name =models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age =models.PositiveIntegerField ()
    dob =models.DateField()
    allergies = models.TextField()
    doctor_number = models.CharField(max_length=50)
    other = models.TextField()
    image = models.ImageField(upload_to='dependency_profile/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' '+ self.last_name
    
    class Meta:
        ordering = ["-timestamp",]
        verbose_name_plural = "Dependencies(students)"

class Video (models.Model):
    dependent = models.ForeignKey(Dependent,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    video_link = models.URLField()
    sport_category= models.ForeignKey(SportsCategory,on_delete=models.CASCADE)
    notes = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dependent.first_name

    class Meta:
        ordering = ["-timestamp",]
        verbose_name_plural = "Dependencies Videos"
