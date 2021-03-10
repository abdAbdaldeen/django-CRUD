from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    phone = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
