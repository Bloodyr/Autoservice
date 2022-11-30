from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Auto, Order, Part, PartsPrice, JobPrice, Jobtype
from .forms import AutoForm, AdditionalUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
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

@csrf_exempt
def cars_page(request):
    form = AutoForm()
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('cars_details_page')
    context = {'form':form}
    return render(request, 'mainsite/cars/cars.html', context)


def cars_details_page(request):
    autos = Auto.objects.all()
    context = {'autos':autos}
    return render(request, 'mainsite/cars/cars_detail.html', context)

@csrf_exempt
def settings_page(request):
    user = User.objects.get(username = request.user)
    if request.method == "POST":
        form = AdditionalUserForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form = AdditionalUserForm(instance=request.user)
    context = {'form':form, 'user':user}
    return render(request, 'mainsite/settings.html', context)


def order_info_page(request):
    orders = Order.objects.filter(client=request.user)
    context = {'orders':orders}
    return render(request, 'mainsite/order_info/order_info.html', context)

def order_detail_page(request, pk):
    profile = User.objects.get(username=request.user)
    order = get_object_or_404(Order, pk=pk)
    context = {'order': order, 'profile': profile}
    return render(request, 'mainsite/order_info/order_check.html', context)


def part_list_page(request):
    parts = Part.objects.all()
    context = {'parts':parts}
    return render(request,'mainsite/part/part_list.html', context)


def part_detail_page(request, pk):
    part_type = get_object_or_404(Part,pk=pk)
    parts = PartsPrice.objects.filter(part=part_type)
    context = {'parts':parts, 'part_type': part_type}
    return render(request, 'mainsite/part/part_detail.html', context)


def part_check_page(request, pk):
    part = get_object_or_404(PartsPrice,pk=pk)
    context = {'part':part}
    return render(request, 'mainsite/part/part_check.html', context)


def job_list_page(request):
    jobs = Jobtype.objects.all()
    context = {'jobs':jobs}
    return render(request, 'mainsite/jobs/jobs_list.html',context)


def job_details(request, pk):
    job = get_object_or_404(Jobtype, pk=pk)
    context = {'job':job}
    return render(request, 'mainsite/jobs/job_details.html',context)