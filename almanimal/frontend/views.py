from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return HttpResponse("<h1>INICIO</h1>")


def about(req):
    return HttpResponse("<h1>ACERCA DE</h1>")


def adopt(req):
    return HttpResponse("<h1>ADOPCIÓN</h1>")


def blog(req):
    return HttpResponse("<h1>BLOG</h1>")

def donate(req):
    return HttpResponse("<h1>DONAR</h1>")
