from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

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

def chris(request):
    global orderdict, intorder1, intorder2
    temporderdict = {}
    if request.user.username == "chris":
        try:
            if orderdict is None:
                pass
        except:
            fullnamedict = {'full_name':request.user.username}
            temporderdict = orderdict
            temporderdict.update(fullnamedict)
        return render_to_response('webapp/chris.html', temporderdict)
    else:
        return HttpResponseRedirect('/unauthorised')

def quickorder(request):
    quickrquest = request.POST.get('quickrquest', '')
    

def order(request):
    global intorder1, intorder2
    order1 = request.POST.get('order1', '')
    order2 = request.POST.get('order2', '')
    try:
        order1
    except:
        order1 = 0
    try:
        order2
    except:
        order2 = 0
    order1int = int(order1)
    #    order1int = int(order2)
    intorder1 += order1int
    #    intorder2 += intorder2
    print intorder1
    return HttpResponseRedirect('/yournest')


def yournest(request):
    global intorder1, intorder2, orderdict, user
    #Try if user is authenticated, if not authenticated redirect to /unauthorised
    struser1 = request.user.username
    if struser1 == "":
        return HttpResponseRedirect('/')
        
    try:
        '''
        if user is not None:
            # the password verified for the user
            if user == {}:
                return HttpResponseRedirect('/')
        '''
            
        if request.user.username == "chris":
            return HttpResponseRedirect('/chris')
            print(request.user.username + " was authenticated.")
    except:
        return HttpResponseRedirect('/')
    try:
        fullnamedict = {'full_name':request.user.username}
        temporderdict = orderdict
        temporderdict.update(fullnamedict)
    except:
        orderdict = {}
        temporderdict = orderdict
        temporderdict.update(fullnamedict)
    return render(request, 'webapp/yournest.html', temporderdict)


def auth_view(request):
    global invalid, user, firstloginport
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



def register_success(request):
    return render_to_response('webapp/register_success.html')


def register_page(request):
    return render(request, 'webapp/register.html', )


def hanyuan(request):
    return render(request, 'webapp/hanyuan.html')


def firstlogin(request):
    global firstloginport, notconfirmedbol
    try:
        global authrb
    except:
        pass

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


def schoollinks(request):
    return render(request, 'webapp/schoollinks.html', {'full_name':request.user.username})


def settings(request):
    return render(request, 'webapp/settings.html', {'full_name':request.user.username})
    
def addorder(request):
    global orderdict
    orderad = request.POST.get('orderad', '')
    orderaddict = {len(orderdict) : 0}
    orderdict.update(orderaddict)
    return HttpResponseRedirect('/chris')
    
    