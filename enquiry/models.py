from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=180)
    contact = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

class HomeContact(models.Model):
    name = models.CharField(max_length=180)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.name
           