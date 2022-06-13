from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class File(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
