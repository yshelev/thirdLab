from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from .models import User, Case


def index(request: HttpRequest) -> HttpResponse:
    user = User.objects.get(id=0)
    cases = Case.objects.all()
    return render(request, "csgorun/index.html", context={"user": user, "cases": cases})


def case(request: HttpRequest, name: str) -> HttpResponse:
    user = User.objects.get(id=0)
    case = get_object_or_404(Case, name=name)
    return render(request, 'csgorun/case.html', {"user": user, "case": case})

