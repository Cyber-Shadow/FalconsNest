from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User


def index(request):
    return render(request, "webapp/home.html")


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('webapp/login.html', c)

def auth_view(request):
    global invalid
    invalid = "False"
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if username == "hanyuan":
        return HttpResponseRedirect('/hanyuan')
    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/loggedin')
    else:
        invalid = "True"
        return HttpResponseRedirect('/invalid')


def loggedin(request):
    return render(request, 'webapp/loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    c = {}
    c.update(csrf(request))
    invalid = {"content":"Your account or password is incorrect."}
    c.update(invalid)
    return render_to_response('webapp/login.html', c)


def logout(request):
    auth.logout(request)
    return render_to_response('webapp/logout.html')


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
    return render(request, 'webapp/register.html',)

def hanyuan(request):
    return render(request, 'webapp/hanyuan.html')
