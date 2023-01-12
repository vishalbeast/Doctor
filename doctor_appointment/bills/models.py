from django.db import models


# Create your models here.


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True,default="1")
    patient_name = models.CharField(max_length=200,default="")
    patient_mob_no = models.CharField(max_length=200,default="")
    patient_email =  models.EmailField(max_length=200,default="")

    def __str__(self):
        return self.patient_name


class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=200)
	product_detail = models.CharField(max_length=200)
	product_price = models.IntegerField(default=0)
	
	def __str__(self):
		return self.product_name


class Cust_bill(models.Model):
	patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
	shop_name = "APNI_DUKAAN"
	purchase_date = models.DateTimeField('purchased date')
	total_items = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)
	
	def __str__(self):
		return self.amount



class Inventory(models.Model):
	product = models.OneToOneField('Product', on_delete=models.CASCADE)
	item_present = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.item_present)