from django.db import models

# Create your models here.

class Book(models.Model):

	def __str__(self):
		return self.name + ' written by ' + self.author

	name=models.CharField(max_length=100)
	author= models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	type = models.CharField(max_length=100) 