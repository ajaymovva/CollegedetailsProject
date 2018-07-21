from django.db import models
from rest_framework import routers, serializers, viewsets


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    acronym = models.CharField(max_length=8)
    contact = models.EmailField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    db_folder = models.CharField(max_length=50)
    dropped_out = models.BooleanField(default=False)

    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MockTestMarks(models.Model):
    problem1 = models.IntegerField()
    problem2 = models.IntegerField()
    problem3 = models.IntegerField()
    problem4 = models.IntegerField()
    total = models.IntegerField(default=0)

    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'Student {self.student} marks'


class Teacher(models.Model):
    name = models.CharField(max_length=128)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name