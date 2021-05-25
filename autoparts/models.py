from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=51)
    car = models.CharField(max_length=51)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
