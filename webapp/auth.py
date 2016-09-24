from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from .models import *

def register_success(request):
    return render_to_response('webapp/register_success.html')


def register_page(request):
    return render(request, 'webapp/register.html', )


def auth_view(request):
    global invalid, user, firstloginport
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            studentreg = student.objects.get(student_number=username)
            if not username in student.get.all():
                nonstudent = True
            else:
                nonstudent = False
                
        except:
            invalid = True
            nonstudent = True
            
        try:
            if studentreg.signedup is False and nonstudent is False:
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(username, "", "falcon")
                    user.first_name = studentreg.first_name
                    surnameset = studentreg.surname
                    surnameset = surnameset.lower()
                    surnameset = surnameset.capitalize()
                    user.last_name = surnameset
                    user.save()
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)
                    return HttpResponseRedirect('/firstlogin')
                else:
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)
                    return HttpResponseRedirect('/')
        except:
            pass
        
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)
        
        if username == "hanyuan":
            return HttpResponseRedirect('/hanyuan')
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/yournest')
        else:
            invalid = True
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/error')
        
def logout(request):
    global logouttext
    auth.logout(request)
    logouttext = True
    return HttpResponseRedirect('/')

def register_user(request):
    if request.method == "POST":
        if User.check_password(request.user ,str(request.POST.get('newpw'))):
            request.session['cpwerror'] = 1
            return HttpResponseRedirect('/firstlogin')
        if request.POST.get('newpw') == request.POST.get('confpw'):
            if not len(request.POST.get('newpw')) < 6:
                u = User.objects.get(username=request.user.username)
                u.set_password(request.POST.get('newpw'))
                u.save()    
                user = auth.authenticate(username=request.user.username, password=request.POST.get('newpw'))
                if user is not None:
                    auth.login(request, user)
                    studentreg = student.objects.get(student_number=request.user.username)
                    studentreg.signedup = True
                    studentreg.save()
                    print studentreg.signedup
                    return HttpResponseRedirect('/yournest')
            else:
                request.session['cpwerror'] = 2
        else:
            request.session['cpwerror'] = 3
    else:
        return HttpResponseRedirect('/unauthorised')
    return HttpResponseRedirect('/firstlogin')
    


def firstlogin(request):
    if request.user.username == "":
        return HttpResponseRedirect('/unauthorised')
    pushdict = { 'full_name' : (request.user.first_name + " " + request.user.last_name) }
    try:
        for x in [1,2,3]:
            if request.session['cpwerror'] == x: 
                pushdict.update({'error':x})
    except:
        pass
    finally:
        request.session['cpwerror'] = 0
    pushdict.update(csrf(request))
    return render(request, 'webapp/firstlogin.html', pushdict)


def unauthorisedpage(request):
    return render_to_response('webapp/unauthorised.html')


def login(request):
    global logouttext, invalid
    c = {}
    c.update(csrf(request))
    struser = str(request.user.username)
    if struser != "":
        try:
            studentreg = student.objects.get(student_number=request.user.username)
            if studentreg.signedup is False:
                return HttpResponseRedirect('/firstlogin')
        except:
            pass

        return HttpResponseRedirect('/yournest')
        
    try:
        if logouttext is True:
            if invalid is False:
                logouttextdict = {'content':'You have been logged out.'}
                c.update(logouttextdict)
                logouttext = False

    except:
        logouttext = False

    try:
        if invalid is True:
            invalid = {'content': 'Your account or password is incorrect. Please try again.'}
            c.update(invalid)
            invalid = False
    except:
        pass
    
    return render_to_response('webapp/login.html', c)
    
def changepw(request):                      #Needs optimisation
    if request.method == "POST":
        if not User.check_password(request.user ,str(request.POST.get('oldpw'))):
            request.session['cpwerror'] = 1
            return HttpResponseRedirect('/settings')
        else:
            if request.POST.get('newpw') == request.POST.get('confpw'):
                if not len(request.POST.get('newpw')) < 6:
                    u = User.objects.get(username=request.user.username)
                    u.set_password(request.POST.get('newpw'))
                    u.save() 
                    user = auth.authenticate(username=request.user.username, password=request.POST.get('newpw'))
                    if user is not None:
                        auth.login(request, user)
                        return HttpResponseRedirect('/settings')
                else:
                    request.session['cpwerror'] = 2
            else:
                request.session['cpwerror'] = 3
    else:
        return HttpResponseRedirect('/unauthorised')
    return HttpResponseRedirect('/settings')
    
