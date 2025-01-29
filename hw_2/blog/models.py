from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
