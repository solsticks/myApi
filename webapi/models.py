from django.db import models


# Create your models here.
class employees(models.Model):
    empId = models.IntegerField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.lastName


class product(models.Model):
    Name = models.CharField(max_length=10)
    Description = models.CharField(max_length=250)
    Price = models.IntegerField()