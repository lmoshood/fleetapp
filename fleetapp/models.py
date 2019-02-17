from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=70)
    pasword = models.CharField(max_length=30)
    licenseNum = models.CharField(max_length=30)
    email = models.EmailField()
    DOB = models.DateTimeField()
    def __str__(self):
        return self.username


class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=20)
    status = models.BooleanField()
    plateNum = models.CharField(max_length=10)
    def __str__(self):
        return self.vehicleType

class Rentals(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=1)
    dateRent = models.DateTimeField()
    returnDate = models.DateTimeField()

    
