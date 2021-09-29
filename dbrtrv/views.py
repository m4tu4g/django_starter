from json.decoder import JSONDecodeError
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Fren
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def add(request):
    namein = request.POST.get('first_name')
    Fren(name= namein).save()
    return HttpResponse(f"Added {namein} as fren into DB")

def rtrvdata(request):
    reslist=[]
    for x in Fren.objects.all(): 
        reslist.append(x.name)
    resjson = json.dumps(reslist)
    return HttpResponse(f"{resjson}<br><br>bye frens...")