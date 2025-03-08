from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title