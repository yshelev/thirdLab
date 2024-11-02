import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from .models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
from .services import (
    get_cases_ordered_by_cost, get_case_by_name, get_skins_from_case_with_name_ordered_by_cost,
    get_list_of_random_skins_from_case_with_name, get_random_skin_from_case_with_name, serialize_skin)


def index(request: HttpRequest) -> HttpResponse:
    cases = get_cases_ordered_by_cost()
    return render(request, "csgorun/cases_cs_2.html", context={"cases": cases})

def case(request: HttpRequest, name: str) -> HttpResponse:
    case_ = get_case_by_name(name)
    skins = get_skins_from_case_with_name_ordered_by_cost(name)
    return render(request, f'csgorun/case_page.html', {"skins": skins, "case" : case_})

def case_api(request: HttpRequest, name: str) -> JsonResponse:
    output_container = get_list_of_random_skins_from_case_with_name(name)
    win_skin = serialize_skin(get_random_skin_from_case_with_name(name))
    return JsonResponse({"container": output_container, "win_skin": win_skin}, safe=False)

def custom_logout(request):
    logout(request)
    next_page = request.GET.get('next', '/')
    return redirect(next_page)


