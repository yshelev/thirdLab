from django.db import models

class User(models.Model):
	"""
	fields:
	name, path_to_icon, balance, items
	"""
	name = models.CharField(max_length=50)
	path_to_icon = models.CharField(max_length=500)
	balance = models.DecimalField(decimal_places=2, max_digits=10)
	items = models.JSONField(default=list)

	class Meta:
		pass

	def add_balance(self, additive):
		if additive <= 0:
			raise ValueError("Additive must be greater than zero")

		self.balance += additive

	def subtract_balance(self, subtractive):
		if subtractive <= 0:
			raise ValueError("Subtractive must be greater than zero")

		if self.balance <= 0:
			raise ValueError("Balance must be greater than zero")

		self.balance -= subtractive

	def __repr__(self):
		return f'User {self.name} with balance {self.balance}'


class Case(models.Model):
	name = models.CharField(max_length=50)
	cost = models.DecimalField(decimal_places=2, max_digits=10)
	path_to_icon = models.CharField(max_length=500)
	pull = models.JSONField(default=list)
	class Meta:
		pass

class Skin(models.Model):
	name = models.CharField(max_length=50)
	path_to_icon = models.CharField(max_length=500)
	cost = models.DecimalField(decimal_places=2, max_digits=10)
	class Meta:
		pass