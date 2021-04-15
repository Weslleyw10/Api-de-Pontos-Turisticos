from django.db import models
from django.db.models.fields import AutoField

class Attractions(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    officeHour = models.CharField(max_length=150)
    minAge = models.CharField(max_length=5)
    image = models.ImageField(upload_to='upload', null=True, blank=True)

    def __str__(self):
        return self.name