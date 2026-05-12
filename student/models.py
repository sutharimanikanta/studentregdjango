from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    rolno = models.CharField(unique=True)
    branch = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
