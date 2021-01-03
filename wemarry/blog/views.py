from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from blog.models import Free

import os
import sys
import json
import urllib.request


def index(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'index.html', context)

def freeDetail(request, pk):
    free = Free.objects.get(pk=pk)
    context = {
        'free': free
    }
    return render(request, 'free/index.html', context)

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


def zvtqkh1khz(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'zvtqkh1khz.html', context)
    
def hcju79b6wj(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'hcju79b6wj.html', context)

def bdd2j7z4jm(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'bdd2j7z4jm.html', context)

def x63w3nobli(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'x63w3nobli.html', context)

def ixjwgfi51r(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'ixjwgfi51r.html', context)

def su36ouypf7(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'su36ouypf7.html', context)

def rmb0wcsenb(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'rmb0wcsenb.html', context)

def jz0q1ec0ft(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'jz0q1ec0ft.html', context)

def kngfl72t8a(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'kngfl72t8a.html', context)

def bbgaae2ait(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'bbgaae2ait.html', context)

def xbbp3io7hn(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'xbbp3io7hn.html', context)

def a7mbi0ylf8(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'a7mbi0ylf8.html', context)

def o9oyldim8s(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'o9oyldim8s.html', context)

def y5ongtfol7(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'y5ongtfol7.html', context)

def btpysvz4te(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'btpysvz4te.html', context)

def pbi8utll1m(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'pbi8utll1m.html', context)

def w5xikllbx8(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'w5xikllbx8.html', context)

def zkm2jy93w7(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'zkm2jy93w7.html', context)

def exgxt9nf6u(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'exgxt9nf6u.html', context)

def f2fh3bwvz9(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'f2fh3bwvz9.html', context)