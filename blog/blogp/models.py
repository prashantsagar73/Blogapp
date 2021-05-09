from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.
class post(models.Model):
    title = models.TextField(max_length=150)
    content = models.CharField(max_length=5000)
    date_time= models.DateField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
