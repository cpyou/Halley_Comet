#-*-coding:utf8-*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from bit.models import Url
from django.contrib.auth import authenticate, login, logout
from bit.def_url import short_to_long, long_to_short
from bit.form import *
from bit.def_disp_data import disp_data

def user_regist(req):
    if req.method == "POST":
        uf = UserRegistForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            if user:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserRegistForm()
    return render(req, 'regist.html', {'uf':uf})

def user_login(req):
    if req.method == "POST":
        lf = UserLoginForm(req.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return HttpResponseRedirect('/')
            else :
                return HttpResponseRedirect('/login/')
    else :
        lf = UserLoginForm()
    return render(req, 'login.html', {'lf':lf})

def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/')

def index(req):
    user_data = disp_data()
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            long_url = lu.cleaned_data["long_url"]
            short_url = long_to_short(long_url)
            user_data = disp_data()
            if req.user.is_authenticated():
                username = req.user.username
                user = User.objects.get(username=username)
                user_data = user.url_set.all().order_by('-visit_time')
                short_url_ = Url.objects.get(short_url=short_url)
                user.url_set.add(short_url_)
            return render(req, 'index.html', {'lu': lu, 'user': req.user, 'short_url': short_url, 'long_url': long_url, 'user_data': user_data})
    else:
        lu = UrlForm()
        if req.user.is_authenticated():
            username = req.user.username
            user = User.objects.get(username=username)
            user_data = user.url_set.all().order_by('-visit_time')
    return render(req, 'index.html', {'lu': lu, 'user': req.user, 'user_data': user_data})

def turn(req, short_hash):
    full_long_url = short_to_long(short_hash)
    return HttpResponseRedirect(full_long_url)


