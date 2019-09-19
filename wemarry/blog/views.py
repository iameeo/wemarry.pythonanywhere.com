from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import os
import sys
import json
import urllib.request


def index(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'index.html', context)

def naverShortUrl(request):
    if request.method == 'POST':
        client_id = "tBEh5gd5bHh5BYrI0X3o"
        client_secret = "78w_tVHJ1B"
        newUrl = ""
        encText = urllib.parse.quote(request.POST['url'])
        data = "url=" + encText
        url = "https://openapi.naver.com/v1/util/shorturl"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            newUrl = json.loads(response_body.decode('utf-8'))
            #print(newUrl["result"]["url"])
            #print(response_body.decode('utf-8'))
        #else:
            #print("Error Code:" + rescode)

        return redirect('/naverShortUrl/?data='+newUrl["result"]["url"])

    elif request.method == 'GET':
        context = {     }
        return render(request, 'naverShortUrl.html', context)

def j45ljmm5ec(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'j45ljmm5ec.html', context)


def i9mt35lg3q(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'i9mt35lg3q.html', context)
