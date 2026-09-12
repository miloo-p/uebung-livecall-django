from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .fruit_data_dummy import fruits

# Create your views here.


def start_page_view(request):
    return HttpResponse("Das hat wunderbar geklappt!")


def all_fruit_view(request):
    return JsonResponse(fruits, safe=False)


def single_fruit_view(request, fruit_id):
    return JsonResponse(fruits[fruit_id])
