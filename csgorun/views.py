from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import *


def index(request: HttpRequest) -> HttpResponse:
    cases = Case.objects.all().order_by("cost")
    return render(request, "csgorun/cases_cs_2.html", context={"cases": cases})

def case(request: HttpRequest, name: str) -> HttpResponse:
    user = User.objects.get(id=1)
    return render(request, f'csgorun/case_{name}.html', {"user": user})

