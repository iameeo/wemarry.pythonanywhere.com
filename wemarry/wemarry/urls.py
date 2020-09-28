"""wemarry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from blog.views import index, freeDetail, naverShortUrl, j45ljmm5ec, i9mt35lg3q, zvtqkh1khz, hcju79b6wj, bdd2j7z4jm, x63w3nobli, ixjwgfi51r, su36ouypf7, rmb0wcsenb, jz0q1ec0ft, kngfl72t8a

urlpatterns = [
    url(r'^$', index),
    url(r'^free/(?P<pk>\d+)/$', freeDetail),
    url(r'^naverShortUrl/$', naverShortUrl),
    url(r'^j45ljmm5ec/$', j45ljmm5ec),
    url(r'^i9mt35lg3q/$', i9mt35lg3q),
    url(r'^zvtqkh1khz/$', zvtqkh1khz),
    url(r'^hcju79b6wj/$', hcju79b6wj),
    url(r'^bdd2j7z4jm/$', bdd2j7z4jm),
    url(r'^x63w3nobli/$', x63w3nobli),
    url(r'^ixjwgfi51r/$', ixjwgfi51r),
    url(r'^su36ouypf7/$', su36ouypf7),
    url(r'^rmb0wcsenb/$', rmb0wcsenb),
    url(r'^jz0q1ec0ft/$', jz0q1ec0ft),
    url(r'^kngfl72t8a/$', kngfl72t8a),
]
