from django.db import models
from django.contrib.auth.models import User

class Reviews(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
