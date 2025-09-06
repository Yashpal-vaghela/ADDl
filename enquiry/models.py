from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=180)
    contact = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
         return f"{self.name} - {self.email}"

class ChatEnquiry(models.Model):
    name = models.CharField(max_length=180)
    email = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
         return f"{self.name} - {self.email}"
           