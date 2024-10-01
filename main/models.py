import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    coquetteness = models.TextField()

    def __str__(self):
         return self.name

# DEMO ANSWER
# class Project(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   # name = models.CharField(max_length=255)
    
   # def __str__(self):
      #   return self.name
    
#class Employee(models.Model):
  #  department = models.CharField(max_length=100)
    #projects = models.ManyToManyField(Project)
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    
   # def __str__(self):
     #   return self.user.username
    