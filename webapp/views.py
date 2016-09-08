from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf


def chris(request):
    global ordrdct, ordernamedict
    chrisdict = {}
    try:
        print ordernamedict
    except:
        pass
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
        print chrisdict
        return render_to_response('webapp/chris.html', chrisdict)
    else:
        return HttpResponseRedirect('/unauthorised')

def quickorder(request):
    quickrquest = request.POST.get('quickrquest', '')
    




def yournest(request):
    global ordernamedict,  ordrdct, user
    #Try if user is authenticated, if not authenticated redirect to /unauthorised
    yourdict = {}
    struser1 = request.user.username
    if struser1 == "":
        return HttpResponseRedirect('/')
        
    try:
        if request.user.username == "chris":
            print(request.user.username + " was authenticated.")
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

def schoollinks(request):
    return render(request, 'webapp/schoollinks.html', {'full_name':request.user.username})


def settings(request):
    return render(request, 'webapp/settings.html', {'full_name':request.user.username})
    
def menu(request):
    return render(request, 'webapp/menu.html', {'full_name':request.user.username})    
    
    
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
        ordrdct = {}
        ordrdct.update(tmporderdict)
    
    try:
        ordernamedict.update(tmpond)
    except:
        ordernamedict = {}
        ordernamedict.update(tmpond)
        
    print ordernamedict
    print ordrdct
    
    return HttpResponseRedirect('/chris')
    
def delorder(request):
    global ordrdct, ordernamedict
    orderdel = request.POST.get('delorder', '')
    delname = "name" + str(orderdel)
    delint = "int" + str(orderdel)
    del ordernamedict[delname]
    del ordrdct[delint]
    
    return HttpResponseRedirect('/chris')

def order(request):
    global  ordrdct
    print  ordrdct
    order1 = request.POST.get('orderval', '')
    order2 = order1[-1:]
    print order2
    ordrdctadder =  ordrdct['1']
    print  ordrdctadder
    #orderdictadder = int(orderdictadder) + 1
    return HttpResponseRedirect('/yournest')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    