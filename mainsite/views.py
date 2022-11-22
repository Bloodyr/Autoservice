from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home_page(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'mainsite/home_page.html', context)
    else:
        return redirect('login')


@csrf_exempt
def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'mainsite/reg_auth/registration.html', context)


@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'mainsite/reg_auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_page')