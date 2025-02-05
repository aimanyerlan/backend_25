from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField()

    def __str__(self):
        return self.title