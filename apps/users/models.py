from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.title + ' ' + self.user.username