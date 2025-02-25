from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Thread(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    picture = models.FileField(upload_to="media/")
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
