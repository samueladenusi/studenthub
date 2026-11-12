from django.db import models

# Create your models here.

class Student(models.Model):
    
    GENDER_CHOICES = [
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=150)
    level = models.IntegerField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.matric_number}'