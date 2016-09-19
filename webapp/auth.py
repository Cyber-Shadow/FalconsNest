from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf

def register_success(request):
    return render_to_response('webapp/register_success.html')


def register_page(request):
    return render(request, 'webapp/register.html', )


def auth_view(request):
    global invalid, user, firstloginport
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username).exists():
            pass
        else:
            strpassword = str(password)
            if strpassword == "falcon":
                firstloginport = username
                return HttpResponseRedirect('/firstlogin')
    
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
    global notconfirmedbol
    try:
        global authrb
    except:
        pass

    if request.method == 'POST':
        username = authrb
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')
        print password
        if password == confirm:
            user = User.objects.create_user(username, "", password)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect('/register_success')
        else:
            notconfirmedbol = True
            
            return HttpResponseRedirect('/firstlogin')

    else:
        return HttpResponseRedirect('/unauthorised')
    args = {}
    args.update(csrf(request))

    return HttpResponseRedirect('/unauthorised')


def firstlogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/unauthorised')

    try:
        if firstloginport is None:
            return HttpResponseRedirect('/unauthorised')
    except:
        pass

    try:
        firstloginoff = firstloginport
        authrb = firstloginoff

    except:
        firstloginoff = None
    
    try:
        notconfirmedbol
    except:
        notconfirmedbol = False
            
    if notconfirmedbol is True:
        notconfirmedbol = False
        c = {}
        c.update(csrf(request))
        tempdict = {'firsttimeuser':firstloginoff, 'invalid':"Your passwords did not match."}
        c.update(tempdict)
        return render(request, 'webapp/firstlogin.html', c)
    
    c = {}
    c.update(csrf(request))
    tempdict = {'firsttimeuser':firstloginoff}
    c.update(tempdict)
    return render(request, 'webapp/firstlogin.html', c)


def unauthorisedpage(request):
    return render_to_response('webapp/unauthorised.html')


def login(request):
    global logouttext, invalid
    c = {}
    c.update(csrf(request))
    struser = str(request.user.username)
    if struser != "":
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
