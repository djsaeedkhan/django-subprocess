from subprocess import Popen, PIPE
from django.shortcuts import render

from django.shortcuts import render,HttpResponse
import subprocess

def home1(request):
    return render(request,"index.html",context=None)

def home(request):
    out = subprocess.Popen(["ls","saeed","-l"], stdout=subprocess.PIPE)
    r = out.communicate()
    print (r)
    return HttpResponse(r)