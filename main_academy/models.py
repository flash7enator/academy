from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("Дата завершення не може бути раніше початку")

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, unique=True)
    phone = models.CharField(max_length=20)
    url_link = models.URLField(blank=True)
    date_of_birth = models.DateField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"