from django.contrib import admin
from .models import Patient, Product, Cust_bill, Inventory
# Register your models here.
admin.site.register(Patient)
admin.site.register(Product)
admin.site.register(Cust_bill)
admin.site.register(Inventory)