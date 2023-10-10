from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name

class Car(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='car_categ')
    name = models.CharField('Car name', max_length=60)
    price = models.PositiveIntegerField('Car price')

    def __str__(self):
        return self.name