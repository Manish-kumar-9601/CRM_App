 
from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email = models.EmailField(max_length=40)
    phone=models.CharField(max_length=13)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    zipcode=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    