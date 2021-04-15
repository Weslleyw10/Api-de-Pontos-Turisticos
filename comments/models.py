from django.db import models
from django.db.models.fields import AutoField
from django.contrib.auth.models import User

class Comments(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name