from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf

def chris(request):
    global ordrdct, ordernamedict
    chrisdict = {}
    
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
        return render_to_response('webapp/chris.html', chrisdict)
    else:
        return HttpResponseRedirect('/unauthorised')

def quickorder(request):
    quickrquest = request.POST.get('quickrquest', '')
    
def yournest(request):
    global ordernamedict,  ordrdct, user
    #Try if user is authenticated, if not authenticated redirect to /unauthorised
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
        
    return render(request, 'webapp/yournest.html', yourdict)
    

def hanyuan(request):
    return render(request, 'webapp/hanyuan.html')
    
def (request):
    return render(request, 'webapp/dirran.html')

def schoollinks(request):
    return render(request, 'webapp/schoollinks.html', {'full_name':request.user.username})

def settings(request):
    return render(request, 'webapp/settings.html', {'full_name':request.user.username})
    
def menu(request):
    global menua, menub, menuc
    pushdict = {"full_name":request.user.username}
    if request.user.username == "chris":
        return HttpResponseRedirect('/chrismenu')
    try: 
        pushdict.update({"menua" : menua})
    except:
        pass
    try: 
        pushdict.update({"menub" : menub})
    except:
        pass
    try: 
        pushdict.update({"menuc" : menuc})
    except:
        pass
    return render(request, 'webapp/menu.html', pushdict)  
    
def chrismenu(request):
    global menua, menub, menuc
    if request.user.username != "chris":
        return HttpResponseRedirect('/menu')
    pushdict = {"full_name":request.user.username}
    try: 
        pushdict.update({"menua" : menua})
    except:
        pass
    try: 
        pushdict.update({"menub" : menub})
    except:
        pass
    try: 
        pushdict.update({"menuc" : menuc})
    except:
        pass
    return render(request, 'webapp/chrismenu.html', pushdict)    
    
    
def about(request):
    return render(request, 'webapp/about.html', {'full_name':request.user.username})    
    
def addorder(request):
    global ordrdct, ordernamedict
    orderad = request.POST.get('addorder', '')
    try:
        onl = str(len(ordernamedict))
    except NameError:
        onl = str(0)
    
    tmporderdict = {'int' + onl : 0}
    tmpond = {'name' + onl : str(orderad)}
   
    try:
        ordrdct.update(tmporderdict)
    except:
        ordrdct = tmporderdict
    
    try:
        ordernamedict.update(tmpond)
    except:
        ordernamedict = tmpond
        
    return HttpResponseRedirect('/chris')
    
def delorder(request):
    global ordrdct, ordernamedict
    orderdel = request.POST.get('delorder', '')
    delname = "name" + str(orderdel)
    delint = "int" + str(orderdel)
    print delname
    print delint
    del ordernamedict[delname]
    del ordrdct[delint]
    return HttpResponseRedirect('/chris')
    
def addmenu(request):
    global menua, menub, menuc
    if str(request.POST.get('menutype', '')) == "a":
        try:
            menua.append(str(request.POST.get('menuadd', '')))
        except:
            menua = [str(request.POST.get('menuadd', ''))]
    elif str(request.POST.get('menutype', '')) == "b":
        try:
            menub.append(str(request.POST.get('menuadd', '')))
        except:
            menub = [str(request.POST.get('menuadd', ''))]
    elif str(request.POST.get('menutype', '')) == "c":
        try:
            menuc.append(str(request.POST.get('menuadd', '')))
        except:
            menuc = [str(request.POST.get('menuadd', ''))]
    else:
        return None
    print menua
    return HttpResponseRedirect('/chris')

def delmenu(request):
    global menua, menub, menuc
    if str(request.POST.get('menutype', '')) == "a":
        try:
            menua.remove(str(request.POST.get('rmmenu', '')))
        except:
            pass
    elif str(request.POST.get('menutype', '')) == "b":
        try:
            menub.append(str(request.POST.get('rmmenu', '')))
        except:
            pass
    elif str(request.POST.get('menutype', '')) == "c":
        try:
            menuc.append(str(request.POST.get('rmmenu', '')))
        except:
            pass
    else:
        return None
    print menua
    return HttpResponseRedirect('/chrismenu')

def order(request):
    global  ordrdct
    order1 = request.POST.get('orderval', '')
    order2 = order1[-1:]
    ordrdctadder =  ordrdct['1']
    #orderdictadder = int(orderdictadder) + 1
    return HttpResponseRedirect('/yournest')    