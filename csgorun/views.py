from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *


def index(request: HttpRequest) -> HttpResponse:
    cases = Case.objects.all().order_by("cost")
    return render(request, "csgorun/cases_cs_2.html", context={"cases": cases})

def case(request: HttpRequest, name: str) -> HttpResponse:
    case_ = Case.objects.get(name=name)

    skins = []

    for skin_id in case_.pull:
        skins.append(Skin.objects.get(id=skin_id))

    skins.sort(key=lambda skin: skin.cost, reverse=True)

    return render(request, f'csgorun/case_{name}.html', {"skins": skins})

