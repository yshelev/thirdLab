from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from .models import User, Case


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "csgorun/cases_cs_2.html")



def case(request: HttpRequest, name: str) -> HttpResponse:
    user = User.objects.get(id=1)
    case = get_object_or_404(Case, name=name)
    return render(request, 'csgorun/cases_cs_2.html', {"user": user, "case": case})

