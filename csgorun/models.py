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

	def add_balance(self, additive: int|float = 0) -> bool:
		"""
		Raise value error if additive is negative.\n
		return True if additive is added else return False.

		:param additive:
		:return:
		"""
		if additive < 0:
			try:
				raise ValueError("Additive must be greater than zero")
			finally:
				return False

		self.balance += additive

		return True

	def subtract_balance(self, subtractive: int|float = 0) -> bool:
		"""
		Raise value error if subtractive is negative\n
		Raise value error if balance is negative or equal to zero.\n
		return True if subtractive is subtracted else return False.

		:param subtractive:
		:return:
		"""
		if subtractive < 0:
			try:
				raise ValueError("Subtractive must be greater than zero")
			finally:
				return False

		if self.balance < 0:
			try:
				raise ValueError("Balance must be greater than zero")
			finally:
				return False

		self.balance -= subtractive
		return True

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