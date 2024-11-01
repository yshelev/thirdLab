import datetime

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, steamid, password, **extra_fields):
        """
        Creates and saves a User with the given steamid and password.
        """

        if not steamid:
            raise ValueError('The given steamid must be set')
        print(steamid, password)
        user = self.model(steamid=steamid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, steamid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(steamid, password, **extra_fields)

    def create_superuser(self, steamid, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(steamid, password, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    fields:\n
    name, path_to_icon, balance, items\n
    methods:\n
    add_balance,
    substract_balance,
    add_item
    """
    email = models.CharField(max_length=255)
    steamid = models.CharField(max_length=17, unique=True)
    personalname = models.CharField(max_length=255)
    profileurl = models.CharField(max_length=300)
    avatar = models.CharField(max_length=255)
    avatarmedium = models.CharField(max_length=255)
    avatarfull = models.CharField(max_length=255)

    USERNAME_FIELD = 'steamid'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        pass

class SiteUser(models.Model):
    steamUser: User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    balance: int = models.IntegerField(default=0)
    items: list = models.JSONField(default=list)  # items_ids
    password: str = models.CharField(max_length=500, default="1")
    last_login: datetime.datetime = models.DateTimeField(default=datetime.datetime.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def get_short_name(self):
        return self.steamUser.personalname

    def get_full_name(self):
        return self.steamUser.personalname

    def add_item(self, item_id):
        try:
            Skin.objects.get(item_id)
            self.items.append(item_id)
        except Skin.DoesNotExist:
            raise IndexError("Skin does not exist")

        except Exception as e:
            raise Exception(f"unknown error: {e}")

    def add_balance(self, additive: int | float = 0) -> bool:
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

    def subtract_balance(self, subtractive: int | float = 0) -> bool:
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
        return f'User {self.steamUser.personalname} with balance {self.balance}'

class Case(models.Model):
    name: str = models.CharField(max_length=50)
    cost: int = models.IntegerField()
    path_to_icon: str = models.CharField(max_length=500)
    pull: list = models.JSONField(default=list)

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

class Rarity(models.Model):
    UNCOMMON: int = 1
    RARE: int = 3
    LEGENDARY: int = 5
    ANCIENT: int = 7

    RARITY_CHOICES = {
        UNCOMMON: "uncommon",
        RARE: "rare",
        LEGENDARY: "legendary",
        ANCIENT: "ancient",
    }

    index: int = models.IntegerField(choices=RARITY_CHOICES, unique=True)
    name: str = models.CharField(max_length=50, unique=True, blank=True, null=True)


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
    rarity: Rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE, null=True, blank=True)
    cost: int = models.IntegerField()
    class Meta:
        pass