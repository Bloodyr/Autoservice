from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Auto, Order, Part, PartsPrice, JobPrice, Jobtype, ClientAuto, Bill, PaymentType
from .forms import AutoForm, AdditionalUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


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
    context = {'orders':orders, }
    return render(request, 'mainsite/order_info/order_info.html', context)

def order_detail_page(request, pk):
    profile = User.objects.get(username=request.user)
    order = get_object_or_404(Order, pk=pk)
    payment_type = PaymentType.objects.get(pk=1)
    total = 0
    for job in order.job_list.all():
        total += job.price
    bill = Bill.objects.get_or_create(order=order, payment_date=datetime.date.today(),payment_type=payment_type ,total=total)
    context = {
        'order': order, 
        'profile': profile,
        'total': total,
    }

    return render(request, 'mainsite/order_info/order_check.html', context)


def order_pay(request, total,pk):
    order = get_object_or_404(Order, pk=pk)
    bill = get_object_or_404(Bill,total=total)
    context = {
        'order':order,
        'bill':bill,
    }
    return render(request, 'mainsite/order_info/order_pay.html',context)


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


def bill_page(request):
    order = Order.objects.filter(client=request.user).order_by('id')[0]
    context = {'order':order}
    return render(request, 'mainsite/order_info/bill_page.html',context)

    
@csrf_exempt
def creation_order_page(request):
    jobs = Jobtype.objects.all()
    auto = ClientAuto.objects.filter(client=request.user)

    if request.method == "POST":
        order = Order.objects.create(
            order_date = datetime.date.today(),
            client = request.user,
            status = 2,
            car =  ClientAuto.objects.get(id=request.POST.get("car")) 
        )
        for job in jobs:
            if request.POST.get(job.job_name):
                order.job_list.add(Jobtype.objects.get(id = request.POST.get(job.job_name))) 
        return redirect('bill_page')
            

    context = {'jobs': jobs, 'auto':auto}
    return render(request,'mainsite/order_info/creation_order.html',context)


def recipe(request, pk):
    profile = User.objects.get(username=request.user)
    order = get_object_or_404(Order, pk=pk)
    total = 0
    for job in order.job_list.all():
        total += job.price
    context = {
        'order': order, 
        'profile': profile,
        'total': total,
        
    }    
    return render(request,'mainsite/order_info/order_billing.html' ,context)