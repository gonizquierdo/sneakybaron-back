from django.shortcuts import render
from django.http import HttpResponse
from .models import Summoner


# Create your views here.
def new_waitlist_summoner(request):
    name=request.GET.get('name')
    if request.method == "POST":
        print(request)
    return HttpResponse("<h1>Hola " + name+ "</h1>")

# Returns patch info as is treated now (JSON)
def get_patch_info(request):
    return HttpResponse("<h1>Hola</h1>")
