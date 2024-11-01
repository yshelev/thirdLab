import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from .models import *


def index(request: HttpRequest) -> HttpResponse:
    cases = Case.objects.all().order_by("cost")
    return render(request, "csgorun/cases_cs_2.html", context={"cases": cases})

def case(request: HttpRequest, name: str) -> HttpResponse:
    print(name)
    case_ = Case.objects.get(name=name)

    skins = []

    for skin_id in case_.pull:
        skins.append(Skin.objects.get(id=skin_id))

    skins.sort(key=lambda skin: skin.cost, reverse=True)

    return render(request, f'csgorun/case_{name}.html', {"skins": skins})

def case_api(request: HttpRequest, name: str) -> JsonResponse:
    case_ = Case.objects.get(name=name)
    output_container: list = []
    print(case_.pull)
    for i in range(50):
        output_container.append(random.choice(case_.pull))

    # output_container = list(map(Skin.objects.get()))
    return JsonResponse(output_container, safe=False)

