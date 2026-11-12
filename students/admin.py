from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)

# This makes our Student model accessible through Django's built-in administration interface.