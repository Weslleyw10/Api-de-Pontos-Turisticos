from django.db import models
from django.db.models.deletion import CASCADE
from attractions.models import Attractions
from comments.models import Comments
from reviews.models import Reviews
from address.models import Address

class TouristSpots(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=CASCADE,  null=True)
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions,  null=True)
    comment = models.ManyToManyField(Comments,  null=True)
    image = models.ImageField(upload_to='upload', null=True, blank=True)


    def __str__(self):
        return self.name
