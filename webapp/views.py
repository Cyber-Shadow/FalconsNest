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
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')


def loggedin(request):
    return render(request, 'webapp/loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('webapp/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('webapp/logout.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.objects.create_user(username, password)
        if username is not None():
            if password is not None():
                user.save()
                return HttpResponseRedirect('/register_success')

    else:
        return None
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')

def register_page(request):
    return render(request, 'webapp/register.html',)
