from django.db import models

# Create your models here.
from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mc_number = models.CharField(max_length=50)
    query = models.TextField()
    contact_method = models.CharField(max_length=10, choices=[('phone', 'Phone'), ('email', 'Email')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class Reach(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name