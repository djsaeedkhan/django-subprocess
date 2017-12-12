from subprocess import Popen, PIPE
from django.shortcuts import render

from django.shortcuts import render,HttpResponse
import subprocess

def home(request):
    process = subprocess.Popen("ls -l | awk '{ print  $1 , $2 , $5 , $6 , $7 , $8 , $9 }'", cwd='/home/parspooyesh-kashan4/', stdin=subprocess.PIPE,shell=True,stdout=subprocess.PIPE)
    out, err = process.communicate()

    list,ii={},0
    data=out.decode('utf-8').split('\n')
    for i in data:
        if(i!=""):
            list[ii]=i.split(' ')
            ii += 1
    list.pop(0, None)
    return render(request,"index.html",context={"list":list})