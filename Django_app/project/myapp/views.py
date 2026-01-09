from django.shortcuts import render
# from django.http import HttpResponse
import json
import csv
import io
import zipfile

# Create your views here.

def landing(request):
    return HttpResponse("this is django page")


