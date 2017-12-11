from subprocess import Popen, PIPE
from django.shortcuts import render

from django.shortcuts import render,HttpResponse
import subprocess

def home(request):
    #ls -l | awk '{ print $5, $9 }'
    commands = ''
    process = subprocess.Popen(['ls','-l'],
                               cwd='/home/parspooyesh-kashan4/saeed/django',
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    print(out.decode('utf-8'))
    return HttpResponse(out.decode('utf-8'))