from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('login')
        else:
            return render(request, 'booking/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'booking/register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username= request.POST["username"]
        password =  request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'booking/login.html')
    return render(request, 'booking/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

@login_required
def home(request):
    user = request.user.username
    return render(request, 'booking/home.html', {'username':user} )