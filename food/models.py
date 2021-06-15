"""from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    food_logo = models.FileField()

    def __str__(self):
        return self.name

class Myfoodrating(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

class MyfoodList(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    addtocart = models.BooleanField(default=False)"""