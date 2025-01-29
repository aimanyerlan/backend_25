from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    producer = models.CharField(max_length=200)
    duration = models.IntegerField()  

    def __str__(self):
        return self.title
