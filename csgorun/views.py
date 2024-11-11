from json import JSONDecoder

from django.contrib.auth import logout
from django.http import HttpRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from urllib3 import request

from .serializers import SkinSerializer
from .services import (
    get_cases_ordered_by_cost, get_case_by_name, get_skins_from_case_with_name_ordered_by_cost,
    get_list_of_random_skins_from_case_with_name, get_random_skin_from_case_with_name, serialize_skin,
    check_if_user_can_open_case_with_name, update_user_after_buy_case_with_name, get_skins_from_user_with_id,
    get_skin_by_attributes, get_skin_by_id
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


@csrf_exempt
def sell_skins(request: HttpRequest) -> HttpResponse:
    try:
        skins_to_sell = JSONDecoder().decode(request.body.decode())
        print(skins_to_sell)
        for skin_dict in skins_to_sell:
            skin_name = skin_dict["skin_name"]
            gun_name = skin_dict["gun_name"]
            skin_quality = skin_dict["skin_quality"]
            skin_souvenir = skin_dict["is_souvenir"]
            skin_statTrack = skin_dict["is_statTrack"]
            skin_cost = skin_dict["skin_cost"]
            skin = get_skin_by_attributes(
                skin_name,
                gun_name,
                skin_quality,
                skin_souvenir,
                skin_statTrack,
                skin_cost
            )
            request.user.siteuser.items.remove(skin.id)
            request.user.siteuser.balance += skin.cost

            request.user.siteuser.save()
    except Exception as e:
        print(str(e))
        return JsonResponse({"error": str(e)}, safe=False, status=400)
    return JsonResponse(
        {
            "user_skins": [SkinSerializer(get_skin_by_id(skin_id)).data for skin_id in request.user.siteuser.items],
            "user_balance": request.user.siteuser.balance
        }
    )