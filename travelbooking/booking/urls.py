from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home', permanent=False), name='root'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('profile/', views.update_profile, name='profile'),
    path('travels/',views.travel_list, name = 'travel_list'),
    path('travel/<int:id>/', views.travel_detail, name='travel_detail'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]