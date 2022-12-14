from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

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
            return redirect('articles:new_home')
        else:
            messages.error(request, 'User does not exist')

    context = {'page':page}
    return render(request, 'account/login_signup.html',context)


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
            return redirect('articles:new_home')
        else:
            messages.error(request,"An error occurred during registration")
    return render(request,'account/login_signup.html',{'form':form})
