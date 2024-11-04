import json
import random

from django.db.models import QuerySet

from .models import Case, Skin
from .serializers import SkinSerializer


def get_cases_ordered_by_cost() -> QuerySet:
	return Case.objects.all().order_by('cost')

def get_case_by_name(name: str) -> Case:
	return Case.objects.get(name=name)

def get_skin_by_id(id_: int) -> Skin:
	return Skin.objects.get(id=id_)

def get_skins_from_case_with_name_ordered_by_cost(name: str) -> list[Skin]:
	case_ = get_case_by_name(name)
	skins = []

	for skin_id in case_.pull:
		skins.append(Skin.objects.get(id=skin_id))

	skins.sort(key=lambda skin: skin.cost, reverse=True)

	return skins

def serialize_skin(skin: Skin) -> dict:
	skin_serializer_ = SkinSerializer(skin)
	return skin_serializer_.data

def dict_to_json(dct: dict) -> str:
	return json.dumps(dct, default=serialize_skin)

def get_list_of_random_skins_from_case_with_name(name: str) -> list:
	case_ = get_case_by_name(name)
	output_container: list = []
	for i in range(100):
		output_container.append(serialize_skin(get_skin_by_id(random.choice(case_.pull))))

	return output_container

def get_random_skin_from_case_with_name(name: str):
	case_ = get_case_by_name(name)
	pull_ = case_.pull
	return Skin.objects.get(id=random.choice(pull_))
