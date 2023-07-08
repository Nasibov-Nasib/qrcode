from django.shortcuts import render
from qrcode import *
from django.conf import settings
import os

def error_404_view(request, exception):
    

    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

def index(request):
    data=''
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        img.save("static/image/test.png")   
        
    return render(request,"main/index.html",{'data':data})