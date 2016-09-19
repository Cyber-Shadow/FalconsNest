#Imports
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from .models import *
from django.db.models import F

def chris(request):                                #Main Chris page
    if request.user.username == "chris":
        chrisdict = {}
        orderlist = ordermodel.objects.all()    
        try:
            fullnamedict = {'full_name':request.user.username}
            chrisdict =  dict(ordrdct)
            chrisdict.update(ordernamedict)
        except:
            ordrdct = {}
        finally:
            chrisdict.update(fullnamedict)
            chrisdict.update(csrf(request))
            chrisdict.update({'orderlist':orderlist})
        return render_to_response('webapp/chris.html', chrisdict)
    else:
        return HttpResponseRedirect('/unauthorised')

    
def yournest(request):
    #Try if user is authenticated, if not authenticated redirect to /unauthorised
    menulist = ordermodel.objects.all()
    yourdict = {}
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
        
    try:
        if request.user.username == "chris":
        
            return HttpResponseRedirect('/chris')

    except:
        return HttpResponseRedirect('/')
        
    try:
        fullnamedict = {'full_name':request.user.username}
        yourdict = ordrd
        yourdict.update(ordernamedict)
    except:
        ordrd = {}
        yourdict = {}
    finally:
        yourdict.update(fullnamedict)
        yourdict.update(csrf(request))
        yourdict.update({'menulist':menulist})
    return render(request, 'webapp/yournest.html', yourdict)
    

def hanyuan(request):
    return render(request, 'webapp/hanyuan.html')
 
def error(request):
    return render(request, 'webapp/error.html')
    
def dirran(request):
    return render(request, 'webapp/dirran.html')

def schoollinks(request):
    if request.user.is_authenticated:
        return render(request, 'webapp/schoollinks.html', {'full_name':request.user.username})
    else:
        return HttpResponseRedirect('/error')

def settings(request):
    if request.user.is_authenticated: 
        pushdict = { 'full_name' : request.user.username,
                     'orderlist' : ordermodel.objects.all(),
                } 
        return render(request, 'webapp/settings.html', pushdict)
    
    else:
        return HttpResponseRedirect('/unauthorised')
    
def menu(request):
    if request.user.username == "chris":
        return HttpResponseRedirect('/chrismenu')
    pushdict = { "full_name" : request.user.username,
                 "orderlist" : ordermodel.objects.all(),
                 "unorderablelist" : menumodel.objects.filter(category = "u"),
                 "snackslist" : menumodel.objects.filter(category = "sn"),
                 "drinkslist" : menumodel.objects.filter(category = "d"),
                 "sweetslist" : menumodel.objects.filter(category = "s"),
                 "icelist" : menumodel.objects.filter(category = "i"),
                 }

    return render(request, 'webapp/menu.html', pushdict)  
    
def chrismenu(request):
    global menua, menub, menuc
    if request.user.username != "chris":
        return HttpResponseRedirect('/menu')
    pushdict = { "full_name" : request.user.username,
                 "orderlist" : ordermodel.objects.all(),
                 "unorderablelist" : menumodel.objects.filter(category = "u"),
                 "snackslist" : menumodel.objects.filter(category = "sn"),
                 "drinkslist" : menumodel.objects.filter(category = "d"),
                 "sweetslist" : menumodel.objects.filter(category = "s"),
                 "icelist" : menumodel.objects.filter(category = "i"),
                 }
    pushdict.update(csrf(request))
    return render(request, 'webapp/chrismenu.html', pushdict)    
    
    
def about(request):
    if request.user.is_authenticated:    
        return render(request, 'webapp/about.html', {'full_name':request.user.username}) 
    else:
        return HttpResponseRedirect('/unauthorised')

def terms(request):
    if request.user.is_authenticated:    
        return render(request, 'webapp/terms.html', {'full_name':request.user.username}) 
    else:
        return HttpResponseRedirect('/unauthorised')    
    
def addorder(request):
    if request.method == 'POST':
        if request.user.username == "chris":
            try:
                orderad = str(request.POST.get('addorder', ''))
            except:
                return HttpResponseRedirect('/error')
            try:
                orderadprice = float(request.POST.get('addorderprice', ''))
            except:
                return HttpResponseRedirect('/error')
            if not ordermodel.objects.filter(name = orderad).exists():
                ordermodel_obj = ordermodel(name=orderad, value = 0, price = orderadprice)
                ordermodel_obj.save()
                return HttpResponseRedirect('/chris')
            else:
                return HttpResponseRedirect('/error')
        else:
            return HttpResponseRedirect("/unauthorised")
    else:
        return HttpResponseRedirect('/error')
  
  

def delorder(request):
    if request.method == 'POST':
        if request.user.username == "chris":
            try:
                orderdel = request.POST.get('delorder', '')
                dlo = ordermodel.objects.get(name = orderdel)
                dlo.delete()
            except:
                return HttpResponseRedirect('/error')
            return HttpResponseRedirect('/chris')
        else:
            return HttpResponseRedirect('/unauthorised')
    else:
        return HttpResponseRedirect('/error')
    
    
def addmenu(request):
    if request.method == 'POST':
        try:
            menuad = str(request.POST.get('menuadd', ''))
        except:
            return HttpResponseRedirect('/error')
        try:
            menuadprice = float(request.POST.get('menuaddprice', ''))
        except:
            return HttpResponseRedirect('/error')
        try:
            menuadtype = str(request.POST.get('menutype', ''))
        except:
            return HttpResponseRedirect('/error')
        if not menumodel.objects.filter(name = menuad).exists():
            try:
                menumodel_obj = menumodel(name=menuad, category = menuadtype, price = menuadprice)
                menumodel_obj.save()
                return HttpResponseRedirect('/chris')
            except:
                return HttpResponseRedirect('/error')
        else:
            return HttpResponseRedirect('/error')
        return HttpResponseRedirect('/chris')
    else:
        return HttpResponseRedirect('/error')


def delmenu(request):
    if request.user.username != "chris":
        return HttpResponseRedirect("/unauthorised")
    menudel = request.POST.get('del', '')
    try:
        menumodel_obj = menumodel.objects.get(name = menudel)
        menumodel_obj.delete()
        return HttpResponseRedirect('/chris')
    except:
        return HttpResponseRedirect('/error')
    return HttpResponseRedirect('/chrismenu')

def order(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            ordernow = str(request.POST.get('ordernow', ''))
            orderamount = int(request.POST.get('orderamount', ''))
            if ordermodel.objects.filter(name=ordernow).exists():
                submitorder = ordermodel.objects.get(name=ordernow)
                submitorder.value = F('value') + orderamount
                submitorder.save()
                return HttpResponseRedirect('/yournest')
            else:
                return HttpResponseRedirect('/error')
        else:
            return HttpResponseRedirect('/unauthorised')
    else:
        return HttpResponseRedirect('/error')


def faveorder(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if not ordermodel.objects.filter(name=str(request.POST.get('faveorder', ''))).exists():
                return HttpResponseRedirect('/error')
            try:
                favemodel_obj = usersetting.objects.get(name=request.user.username)
            except:
                favemodel_obj = usersetting(name=request.user.username, fave = str(request.POST.get('faveorder', '')))
            favemodel_obj.fave = str(request.POST.get('faveorder', ''))
            favemodel_obj.save()
        return HttpResponseRedirect('/settings')
    else:
        return HttpResponseRedirect('/error')
    
    
def quickorder(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                faveorder = usersetting.objects.get(name=request.user.username)
                submitorder = ordermodel.objects.get(name=faveorder.fave)
                submitorder.value = F('value') + 1
                submitorder.save()
                return HttpResponseRedirect('/yournest')
    
            except:
                return HttpResponseRedirect('/error')

            