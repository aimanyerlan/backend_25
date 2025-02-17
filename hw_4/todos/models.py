from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField()
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title