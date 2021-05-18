from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=51)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=51)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=51)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Glass(models.Model):
    name = models.CharField(max_length=51)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
