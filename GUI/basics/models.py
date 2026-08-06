from django.db import models

# Create your models here.
class Employee_Table(models.Model):
    EMP_NAME=models.CharField(max_length=500)
    EMP_DES=models.CharField(max_length=500)
    EMP_Place=models.CharField(max_length=500)


