from django.shortcuts import render
from SOC.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
registered = False
def index(request):
    user_form = UserForm()
    return render(request, 'SOC/index.html',{'registered': registered,
                                                                'user_form': user_form})

def seasons(request):
    return render(request, 'SOC/seasons.html')

def register(request):



    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('User Not Active')
        else:
            return HttpResponse('Invalid Login Details. If you have not registered yet. Register first.')
    else:
        return render(request, 'SOC/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
