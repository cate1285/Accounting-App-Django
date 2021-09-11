from django.contrib import admin
from .models import Product, Order,Staff
from django.contrib.auth.models import Group

admin.site.site_header = "Accounting CM FAMILY"
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Staff)
