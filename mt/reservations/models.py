from django.db import models
from django.contrib.auth.models import User
from tables.models import Table
# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(choices=[
        ("pending", "Pending"), 
        ("confirmed", "Confirmed"), 
        ("canceled", "Canceled")
        ], max_length=1000)
    
    def __str__(self):
        return f"Reservation by {self.user}, table - {self.tabe.number} on {self.date} - {self.status}"