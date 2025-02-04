from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length = 5000)
    author = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    