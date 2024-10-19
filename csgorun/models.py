from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50)
	path_to_icon = models.CharField(max_length=500)
	balance = models.DecimalField(decimal_places=2, max_digits=10)
	items = models.JSONField(default=list)
	class Meta:
		pass

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