from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def index(request: HttpRequest) -> HttpResponse:
	print(request.META)
	return render(request, "csgorun/index.html")