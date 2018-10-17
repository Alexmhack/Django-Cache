from django.db import models

"""
name -> char field
description -> text field
price -> decimal field
timestamp -> date time field
updated -> date time field
"""

class Product(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)
