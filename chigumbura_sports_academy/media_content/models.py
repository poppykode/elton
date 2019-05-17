from django.db import models

# Create your models here.

class SportsCategory(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True,unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp",]
        verbose_name_plural = "SportsCategories"



