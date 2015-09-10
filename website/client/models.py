from django.db import models

# Create your models here.

class company(models.Model):
	name = models.CharField(max_length=30)
 	
	def __str__(self):
		return self.name

class ip(models.Model):
	address = models.CharField(max_length=64)
	company = models.ManyToManyField(company)
	def __str__(self):
		return self.address

