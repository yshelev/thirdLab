import random

from django.db.models import QuerySet

from .models import Case, Skin


def get_cases_ordered_by_cost() -> QuerySet:
	return Case.objects.all().order_by('cost')

def get_case_by_name(name: str) -> Case:
	return Case.objects.get(name=name)

def get_skins_from_case_with_name_ordered_by_cost(name: str) -> list[Skin]:
	case_ = get_case_by_name(name)
	skins = []

	for skin_id in case_.pull:
		skins.append(Skin.objects.get(id=skin_id))

	skins.sort(key=lambda skin: skin.cost, reverse=True)

	return skins

def get_list_of_random_skins_from_case_with_name(name: str) -> list:
	case_ = Case.objects.get(name=name)
	output_container: list = []
	print(case_.pull)
	for i in range(50):
		output_container.append(random.choice(case_.pull))

	# output_container = list(map(Skin.objects.get()))
	return output_container
