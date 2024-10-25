import datetime

from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	"""
	fields:\n
	name, path_to_icon, balance, items\n
	methods:\n
	add_balance,
	substract_balance,
	add_item
	"""
	name: str = models.CharField(max_length=50)
	login_id: str = models.CharField(max_length=50, default="unnique_login")
	path_to_icon: str = models.CharField(max_length=500)
	balance: int = models.IntegerField()
	items: list = models.JSONField(default=list) # items_ids
	password: str = models.CharField(max_length=500, default="1")
	last_login: datetime.datetime = models.DateTimeField(default=datetime.datetime.now)

	USERNAME_FIELD = 'login_id'
	REQUIRED_FIELDS = []

	class Meta:
		pass

	def add_item(self, item_id):
		try:
			Skin.objects.get(item_id)
			self.items.append(item_id)
		except Skin.DoesNotExist:
			raise IndexError("Skin does not exist")

		except Exception as e:
			raise Exception(f"unknown error: {e}")


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
	name: str = models.CharField(max_length=50)
	cost: int = models.IntegerField()
	path_to_icon: str = models.CharField(max_length=500)
	pull: list  = models.JSONField(default=list)
	class Meta:
		pass

class OpenCase(models.Model):
	user: User = models.ForeignKey(User, on_delete=models.CASCADE)
	case: Case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Transaction(models.Model):

	SUBTRACT_TYPE = "sub"
	ADDITIVE_TYPE = "add"

	TRANSACTION_TYPES_CHOICE = {
		SUBTRACT_TYPE: "sub",
		ADDITIVE_TYPE: "add",
	}


	user: User = models.ForeignKey(User, on_delete=models.CASCADE)
	transaction_sum: int = models.IntegerField()
	transaction_type: str = models.CharField(max_length=3, choices=TRANSACTION_TYPES_CHOICE, default=SUBTRACT_TYPE)

class Quality(models.Model):
	BATTLE_SCARED = "BS"
	WELL_WORN = "WW"
	FIELD_TESTED = "FT"
	MINIMAL_WEAR = "MW"
	FACTORY_NEW = "FN"
	QUALITY_CHOICES = {
		BATTLE_SCARED: "battle scared",
		WELL_WORN: "well_worn",
		FIELD_TESTED: "field tested",
		MINIMAL_WEAR: "minimal wear",
		FACTORY_NEW: "factory new",
	}
	name: str = models.CharField(
		max_length=2,
		choices=QUALITY_CHOICES,
		default=BATTLE_SCARED,
		unique=True
	)

	def __str__(self):
		return self.name

class Skin(models.Model):
	is_statTrek: bool = models.BooleanField(default=False)
	is_souvenir: bool = models.BooleanField(default=False)
	quality: Quality = models.ForeignKey(Quality, on_delete=models.CASCADE, default=0)
	name: str = models.CharField(max_length=50)
	gun_name: str = models.CharField(max_length=50, default="_")
	path_to_icon: str = models.CharField(max_length=500)
	cost: int = models.IntegerField()
	class Meta:
		pass