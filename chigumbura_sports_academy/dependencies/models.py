from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL 
# Create your models here.
class Dependent(models.Model):
    guardian = models.name = models.ForeignKey(User,on_delete=models.CASCADE)
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
