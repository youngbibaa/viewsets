from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    number_plates = models.CharField(max_length=10)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.brand} {self.model} {self.number_plates}"


class Employer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    salary = models.IntegerField()
    
    def __str__(self):
        f"{self.first_name} {self.last_name} {self.department}"