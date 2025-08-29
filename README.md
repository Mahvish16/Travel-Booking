# Travel Booking Application

A full-stack **Travel Booking Web Application** built with **Python (Django)** that allows users to search, book, and manage their travel plans seamlessly.  

## Overview
The application provides a user-friendly platform for booking **Flights, Trains, and Buses**, with features for user authentication, travel management, and booking history.  
Frontend is developed using **Django Templates** with **Bootstrap** for a responsive design.  


## Features

### User Management
- User registration, login, and logout (Django authentication).  
- Update and manage user profiles.  

### Travel Options
- View available travel options: Flight, Train, Bus.  
- Travel model includes:
  - Travel ID  
  - Type (Flight, Train, Bus)  
  - Source & Destination  
  - Date & Time  
  - Price & Available Seats  

### Booking
- Book travel options directly.  
- Booking model includes:
  - Booking ID  
  - User (Foreign Key)  
  - Travel Option (Foreign Key)  
  - Number of Seats  
  - Total Price  
  - Booking Date  
  - Status (Confirmed/Cancelled)  

### Manage Bookings
- View current and past bookings.  
- Cancel bookings anytime.  

### Frontend
- Fully responsive UI with Bootstrap.  
- User-friendly pages for:
  - Registration & Login  
  - Travel Listings with Filters (type, source, destination, date)  
  - Booking Forms  
  - Booking History  


## Tech Stack
- Backend: Python, Django  
- Frontend: Django Templates, HTML, CSS, Bootstrap  
- Database: MySQL (recommended) / SQLite (default for local development)  


## Installation & Setup

### 1. Clone the Repository
git clone https://github.com/Mahvish16/Travel-Booking.git
cd travel-booking

### 2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

### 3. Database Setup
Update settings.py to use MySQL (or keep SQLite for local testing).

Run migrations:

python manage.py migrate

### 4. Create Superuser

python manage.py createsuperuser

### 5. Run the Development Server

python manage.py runserver
Now visit http://127.0.0.1:8000/

### Bonus Features
Search and filter travel options by type, destination, and date.

Input validation (e.g., available seats check).

Unit tests for core functionalities.

Deployment-ready on AWS / PythonAnywhere / any cloud platform.

### Project Structure

travelbooking/
│── travelbooking/        # Django project settings
│── travel/               # App for managing travel options
│── booking/              # App for booking management
│── users/                # App for authentication & profiles
│── templates/            # HTML templates
│── static/               # CSS, JS, Bootstrap files
│── manage.py             # Django management script

### Deployment
Can be deployed on AWS EC2, PythonAnywhere, or any cloud provider.

Update ALLOWED_HOSTS & database settings in settings.py before deploying.

### Live Demo
Check out the live application here: https://mahvish.pythonanywhere.com/
