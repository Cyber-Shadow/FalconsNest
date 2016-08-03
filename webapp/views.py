from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

def unauthorisedpage(request):
    return render_to_response('webapp/unauthorised.html')

def index(request):
    return render(request, "webapp/home.html")

def login(request):
    global logouttext, invalid
    if request.user.is_authenticated():
        return HttpResponseRedirect('/yournest')

    c = {}
    c.update(csrf(request))
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
    if request.user.username == "chris":
        try:
            if orderdict is None:
                pass
            elif intorder1 is None:
                pass
        except:
            intorder1 = 0
            intorder2 = 0
            orderdict = {"intorder1": intorder1, "intorder2": intorder2, 'full_name': request.user.username}
        return render_to_response('webapp/chris.html', {"intorder1": intorder1, "intorder2": intorder2, 'full_name': request.user.username})
    else:
        return HttpResponseRedirect('/unauthorised')



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
    global intorder1, intorder2, orderdict
    #Try if user is authenticated, if not authenticated redirect to /unauthorised
    try:
        if user is None:
            return HttpResponseRedirect('/unauthorised')
        elif request.user.username == "":
            return HttpResponseRedirect('/unauthorised')
        elif request.user.username is None:
            return HttpResponseRedirect('/unauthorised')

    except:
        return HttpResponseRedirect('/unauthorised')
    try:
        if user is not None:
            # the password verified for the user
            if user == {}:
                return HttpResponseRedirect('/register')
            else:
                if request.user.username == "chris":
                    return HttpResponseRedirect('/chris')
                print(request.user.username + " was authenticated.")
        else:
            print("The username and password were incorrect.")
    except:
        return HttpResponseRedirect('/register')
    try:
        orderdict = {"intorder1": intorder1, "intorder2": intorder2, 'full_name': request.user.username}
    except:
        intorder1 = 0
        intorder2 = 0
        orderdict = {"intorder1": intorder1, "intorder2": intorder2, 'full_name': request.user.username}
    return render(request, 'webapp/yournest.html', {"intorder1": intorder1, "intorder2": intorder2, 'full_name': request.user.username})


def auth_view(request):
    global invalid, user, firstloginport
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if User.objects.filter(username=username).exists():
        pass
    else:
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
            print "pw != c"

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
    global firstloginport
    try:
        global authrb
    except:
        print "authrb fail"
        #authrb = None
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


    c = {}
    c.update(csrf(request))
    tempdict = {'firsttimeuser':firstloginoff}
    c.update(tempdict)
    return render(request, 'webapp/firstlogin.html', c)


def schoollinks(request):
    return render(request, 'webapp/schoollinks.html')


def settings(request):
    return render(request, 'webapp/settings.html')