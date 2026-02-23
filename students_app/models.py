from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, default='unknown@example.com')  # default avoids prompt
    date_of_birth = models.DateField(default='2000-01-01')  # default avoids prompt

    def __str__(self):
        return f"{self.first_name} {self.last_name}"