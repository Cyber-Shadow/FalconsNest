
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
    c = {}
    c.update(csrf(request))
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
    try:
        global user
    except:
        return HttpResponseRedirect('/register')
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
    global invalid, user
    invalid = "False"
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if User.objects.filter(username=username).exists():
        print "1"
        pass
    else:
        return HttpResponseRedirect('/firstlogin')

    user = auth.authenticate(username=username, password=password)
    if username == "hanyuan":
        return HttpResponseRedirect('/hanyuan')
    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/yournest')
    else:
        invalid = "True"
        return HttpResponseRedirect('/invalid')


def invalid_login(request):
    c = {}
    c.update(csrf(request))
    invalid = {"content": "Your account or password is incorrect. Please try again."}
    c.update(invalid)
    return render_to_response('webapp/login.html', c)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.objects.create_user(username, "", password)
        user.save()
        return HttpResponseRedirect('/register_success')

    else:
        return None
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('webapp/register_success.html')


def register_page(request):
    return render(request, 'webapp/register.html', )


def hanyuan(request):
    return render(request, 'webapp/hanyuan.html')

def firstlogin(request):
    return render(request, 'webapp/firstlogin.html')