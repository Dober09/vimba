
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import MissingPerson,WantedPerson
from .forms import MissingPersonForm,WantedPersonForm
# Create your views here.
# Create your views here.


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username or Password does not exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist')

    context = {'page':page}
    return render(request, 'base/login_signup.html',context)


def logout_page(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"An error occurred during registration")
    return render(request,'base/login_signup.html',{'form':form})

def home(request):
    return render(request,'base/home.html')

def missing_people(request):
    missingPeople = MissingPerson.objects.all()
    context = {
        'missingPeople':missingPeople
    }

    return render(request,'base/missing_people.html',context)

def wanted_people(request):
    wantedPeople = WantedPerson.objects.all()
    context = {
        'wantedPeople':wantedPeople
    }

    return render(request,'base/wanted_people.html',context)

def person_of_intrest(request,pk):
    wanted_person = WantedPerson.objects.get(id=pk)
    tags = wanted_person.tags.all()
    context = {
        'person':wanted_person,
        'tags':tags
    }
    return render(request,'base/person_of_intrest.html',context)

def missing_pep(request,pk):
    missing_person = MissingPerson.objects.get(id=pk)
    context = {
        'person':missing_person,
        
    }
    return render(request,'base/missing_details.html',context)

@login_required(login_url='/login')
def add_missing_person(request):
    form = MissingPersonForm()
    
    if request.method == "POST":
        form = MissingPersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('missing_people')
    context = {
        'form':form
    }
    return render(request, 'base/Add_missing_person.html',context)

@login_required(login_url='/login')
def add_wanted_person(request):

    form = WantedPersonForm()
    if request.method == "POST":
        form = WantedPersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wanted_people')
    context = {
        'form':form
    }
    return render(request, 'base/add_wanted_person.html',context)

@login_required(login_url='/login')
def update_missing(request,pk):
    person = MissingPerson.objects.get(id=pk)
    form = MissingPersonForm(instance=person)

    if request.user != person.host:
        return HttpResponse('Your are not allowed here')

    if request.method == 'POST':
        form = MissingPersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('missing_people')
    context = {'form':form}
    return render(request,'base/add_missing_person.html',context)


@login_required(login_url='/login')
def update_wanted(request,pk):
    person = WantedPerson.objects.get(id=pk)
    form = WantedPersonForm(instance=person)

    if request.user != person.host:
        return HttpResponse('Your are not allowed here')
    
    if request.method == 'POST':
        form = WantedPersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('wanted_people')
    context = {'form':form}
    return render(request,'base/add_wanted_person.html',context)


@login_required(login_url='/login')
def remove_wanted(request,pk):
    obj = WantedPerson.objects.get(id=pk)
    if request.user != obj.host:
        return HttpResponse('Your are not allowed here')
    if request.method == 'POST':
        obj.delete()
        return redirect('wanted_people')
    return render(request,'base/delete.html',{'obj':obj})


@login_required(login_url='/login')
def remove_missing(request,pk):
    obj = MissingPerson.objects.get(id=pk)

    if request.user != obj.host:
        return HttpResponse('Your are not allowed here')
    if request.method == 'POST':
        obj.delete()
        return redirect('missing_people')
    return render(request,'base/delete.html',{'obj':obj})
