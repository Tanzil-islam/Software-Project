from django.db import models

# Create your models here.

class StudentProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    def str(self):
        return self.username
    