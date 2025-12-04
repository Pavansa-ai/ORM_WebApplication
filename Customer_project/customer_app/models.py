from django.db import models
from django.contrib import admin

class Customer(models.Model):
    cust_name = models.CharField(max_length=20,help_text="Enter the customer name")
    cust_id = models.IntegerField(help_text="Enter the customer id")
    cust_dob = models.DateField("Enter the customer dob")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cust_name','cust_id','cust_dob']
    


# Create your models here.
