#Imports
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from .models import *
from django.db.models import F

def chris(request):                                #Main Chris page
    chrisdict = {}
    orderlist = ordermodel.objects.all()
    if request.user.username == "chris":
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

def quickorder(request):                          #Quickorder
    quickrquest = request.POST.get('quickrquest', '')
    
def yournest(request):
    global ordernamedict,  ordrdct, user
    #Try if user is authenticated, if not authenticated redirect to /unauthorised
    menulist = ordermodel.objects.all()
    yourdict = {}
    if request.user.username == "":
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
    return render(request, 'webapp/schoollinks.html', {'full_name':request.user.username})

def settings(request):
    if request.user.username != "": 
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
    return render(request, 'webapp/chrismenu.html', pushdict)    
    
    
def about(request):
    return render(request, 'webapp/about.html', {'full_name':request.user.username})    
    
def addorder(request):
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


def delorder(request):
    if request.user.username == "chris":
        orderdel = request.POST.get('delorder', '')
        print orderdel
        dlo = ordermodel.objects.get(name = orderdel)
        dlo.delete()
        return HttpResponseRedirect('/chris')
    else:
        return HttpResponseRedirect('/unauthorised')
    
    
def addmenu(request):
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

def delmenu(request):
    menudel = request.POST.get('del', '')
    try:
        menumodel_obj = menumodel.objects.get(name = menudel)
        menumodel_obj.delete()
        return HttpResponseRedirect('/chris')
    except:
        return HttpResponseRedirect('/error')
    return HttpResponseRedirect('/chrismenu')

def order(request):
    if request.user.username == "":
        return HttpResponseRedirect('/unauthorised')
    ordernow = str(request.POST.get('ordernow', ''))
    orderamount = int(request.POST.get('orderamount', ''))
    submitorder = ordermodel.objects.get(name=ordernow)
    submitorder.value = F('value') + orderamount
    submitorder.save()
    return HttpResponseRedirect('/yournest')
    
    
def faveorder(request):
    print "fuckyea"
    if request.user.user == "":
        return HttpResponseRedirect('/unauthorised')
    faveorder = str(request.POST.get('faveorder', ''))
    if faveorder in ordermodel.objects.all():
        return HttpResponseRedirect('/error')
    favemodel_obj = favemodel(name=request.user.username, favourite = faveorder)
    favemodel_obj.save()
    
    
    
    