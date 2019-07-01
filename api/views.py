from django.shortcuts import render
from django.http import HttpResponse
from .models import Summoner
from riotwatcher import RiotWatcher, ApiError
import json


# Create your views here.
def new_waitlist_summoner(request):
    name=request.GET.get('name')
    if request.method == "POST":
        print(request)
    return HttpResponse("<h1>Hola " + name+ "</h1>")

# Returns patch info as is treated now (JSON)
def get_patch_info(request):
    return HttpResponse("<h1>Hola</h1>")

def riot_api_test(request, summoner_name):

    watcher = RiotWatcher('RGAPI-39766598-422b-465c-9860-8262a88a3113')

    my_region = 'la2'

    me = watcher.summoner.by_name(my_region, summoner_name)

    return HttpResponse(json.dumps(me), content_type='application/javascript')