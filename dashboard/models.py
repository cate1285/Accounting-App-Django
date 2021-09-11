from django.db import models
from django.contrib.auth.models import User
from django.db.models import  Sum
# Create your models here.
CATEGORY = (
    ('Activities', 'Activities'),
    ('Personal Robin', 'Personal Robin'),
    ('Food', 'Food'),
    ('Recibos', 'Recibos'),
    ('Personal Cate', 'Personal Cate'),
    ('Arriendo', 'Arriendo'),
    ('Proyectos', 'Proyectos'),
    ('Compartidos', 'Compartidos')
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return "{}-{}".format(self.quantity,self.category)

CATEGORY1 = (
    ('Activities', 'Activities'),
    ('Personal', 'Personal'),
    ('Food', 'Food'),
)


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY1, null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'

class Staff(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{}-{}".format(self.quantity,self.category)