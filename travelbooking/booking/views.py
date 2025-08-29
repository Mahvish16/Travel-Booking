from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Travel, Booking
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone

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
def update_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        messages.success(request, 'Profile updated.')
        return redirect('profile')

    return render(request, 'booking/profile.html')


@login_required
def home(request):
    user = request.user.username
    return render(request, 'booking/home.html', {'username':user} )

@login_required
def travel_list(request):
    travels = Travel.objects.all()
    travel_type = request.GET.get('type')
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')

    if travel_type:
        travels = travels.filter(type=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)
    if date:
        travels = travels.filter(date_time__date=date) 

    return render(request, 'booking/travel_list.html', {'travels': travels})

@login_required
def travel_detail(request, id):
    travel = get_object_or_404(Travel, id=id)
    return render(request, 'booking/travel_detail.html', {'travel': travel})


@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(Travel, id=travel_id)

    if request.method == 'POST':
        try:
            number_of_seats = int(request.POST.get('number_of_seats', 1))

            if number_of_seats <= 0:
                messages.error(request, 'Number of seats must be at least 1.')
                return render(request, 'booking/booking_form.html', {'travel': travel})

            if number_of_seats > travel.available_seats:
                messages.error(request, 'Not enough available seats.')
                return render(request, 'booking/booking_form.html', {'travel': travel})

            total_price = travel.price * number_of_seats

            booking = Booking.objects.create(
                user=request.user,
                travel_option=travel,
                number_of_seats=number_of_seats,
                total_price=total_price,
                booking_date=timezone.now().date(),
                status='Confirmed'
            )

            travel.available_seats -= number_of_seats
            travel.save()

            return render(request, 'booking/booking_confirm.html', {'booking': booking})


        except ValueError:
            messages.error(request, 'Invalid number of seats.')

    return render(request, 'booking/booking_form.html', {'travel': travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})
    
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status == 'Confirmed':
        booking.status = 'Cancelled'  
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'Booking cannot be cancelled.')

    return redirect('my_bookings')







    