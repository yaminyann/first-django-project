from django.db import models

# Create your models here.

# Forms Model Here
class UserContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=400)
    