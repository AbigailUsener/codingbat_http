from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.
def near_100(request: HttpRequest, n:int) -> HttpResponse:
    return HttpResponse(abs(n)<100 and abs(n)>=90 or abs(n)<200 and abs(n)>=190)
def splice(request: HttpRequest,given:str) -> HttpResponse:
    word=""
    for i in range(len(given)):
        word = word+given[:i+1]
    return HttpResponse(word)
def animal(request: HttpRequest,thing:bool) -> HttpResponse:
    cat=thing.count("cat")
    dog=thing.count("dog")
    return HttpResponse (cat==dog)
def add(request:HttpRequest,a:int,b:int,c:int)->HttpResponse:
    if a!=c and a!=b and c!=b:
        return HttpResponse(a+b+c)
    if a==c and a==b and c==b:
        return HttpResponse(0)
    if a==b and a!=c or a==b and b!=c:
        return HttpResponse(c)
    if a==c and a!=b or a==b and c!=b:
        return HttpResponse(b)
        