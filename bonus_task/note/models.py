from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2500)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title