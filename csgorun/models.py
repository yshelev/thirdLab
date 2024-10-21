from django.db import models

class User(models.Model):
	"""
	fields:\n
	name, path_to_icon, balance, items\n
	methods:\n
	add_balance,
	substract_balance,
	add_item
	"""
	name: str = models.CharField(max_length=50)
	path_to_icon: str = models.CharField(max_length=500)
	balance: int = models.IntegerField()
	items: list = models.JSONField(default=list) # items_id

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

class Gun(models.Model):
	name = models.CharField(max_length=50, default="ssg08", unique=True)

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

class Skin(models.Model):
	quality: Quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
	gun: Gun = models.ForeignKey(Gun, on_delete=models.CASCADE)
	name: str = models.CharField(max_length=50)
	path_to_icon: str = models.CharField(max_length=500)
	cost: int = models.IntegerField()
	class Meta:
		pass