from django.db import models

# Create your models here.


class Customer (models.Model):
  company_name = models.CharField(max_length=20)
  contact = models.CharField(max_length=20)
  phone_number = models.CharField(max_length=20)
  location = models.CharField(max_length=20)
  number_employees = models.CharField(max_length=10)
