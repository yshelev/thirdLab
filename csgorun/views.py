from django.contrib.auth import logout
from django.http import HttpRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import (
    get_cases_ordered_by_cost, get_case_by_name, get_skins_from_case_with_name_ordered_by_cost,
    get_list_of_random_skins_from_case_with_name, get_random_skin_from_case_with_name, serialize_skin,
    check_if_user_can_open_case_with_name, update_user_after_buy_case_with_name, get_skins_from_user_with_id
)


def index(request: HttpRequest) -> HttpResponse:
    cases = get_cases_ordered_by_cost()
    return render(request, "csgorun/cases_cs_2.html", context={"cases": cases})
@login_required
def profile(request: HttpRequest) -> HttpResponse:
    context = {
        "skins": get_skins_from_user_with_id(request.user.id),
    }
    return render(request, "csgorun/Инвентарь.html", context=context)

def case(request: HttpRequest, name: str) -> HttpResponse:
    context = {
        "skins": get_skins_from_case_with_name_ordered_by_cost(name),
        "case": get_case_by_name(name)
    }
    return render(request, f'csgorun/case_page.html', context)

def open_case_api(request: HttpRequest, name: str) -> JsonResponse:
    if not check_if_user_can_open_case_with_name(request.user, name):
        return JsonResponse({"can_open": False, "container": [], "win_skin": None}, safe=False)
    skin = get_random_skin_from_case_with_name(name)
    user = request.user

    update_user_after_buy_case_with_name(user, name, skin.id)
    data = {
        "can_open": True,
        "new_user_balance": user.siteuser.balance,
        "container": get_list_of_random_skins_from_case_with_name(name),
        "win_skin": serialize_skin(skin)
    }
    return JsonResponse(data, safe=False)

def custom_logout(request):
    logout(request)
    next_page = request.GET.get('next', '/')
    return redirect(next_page)


