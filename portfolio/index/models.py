from django.db import models

# Create your models here.
class Contact_db(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=30)
    Purpose=models.TextField(max_length=300)