from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    user = request.user.username
    return render(request, 'booking/home.html', {'username':user} )

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

