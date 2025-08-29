Travel Booking Application
Overview

This is a Travel Booking Web Application built using Python (Django) that allows users to:

Register, login, and manage their profiles.

View available travel options (Flight, Train, Bus).

Book tickets and manage their bookings.

Cancel bookings and view past reservations.

The frontend is developed using Django Templates and styled with Bootstrap for responsiveness.

Features
User Management

User registration, login, and logout (Django authentication).

Profile update functionality.

Travel Options

Travel model with fields:

Travel ID

Type (Flight, Train, Bus)

Source & Destination

Date and Time

Price & Available Seats

Booking

Users can book travel options.

Booking model includes:

Booking ID

User (Foreign Key)

Travel Option (Foreign Key)

Number of Seats

Total Price

Booking Date

Status (Confirmed/Cancelled)

Manage Bookings

View current and past bookings.

Cancel bookings.

Frontend

Responsive design using Bootstrap.

User-friendly pages for:

Registration & Login

Travel listing with filters (type, source, destination, date).

Booking form.

Booking history.

Tech Stack

Backend: Python, Django

Frontend: Django Templates, HTML, CSS, Bootstrap

Database: MySQL (recommended) / SQLite (default for local development)

Installation & Setup
Clone the Repository
git clone https://github.com/your-username/travel-booking.git
cd travel-booking

Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

Database Setup

Update settings.py to use MySQL (or keep SQLite for local testing).

Run migrations:

python manage.py migrate

Create Superuser
python manage.py createsuperuser

Run the Development Server
python manage.py runserver


Now visit http://127.0.0.1:8000/

Bonus Features

Search and filter travel options by type, destination, and date.

Input validation (e.g., available seats).

Unit tests for key features.

Deployment on AWS / PythonAnywhere / any cloud platform.

Project Structure
travelbooking/
│── travelbooking/        # Django project settings
│── travel/               # App for managing travel options
│── booking/              # App for booking management
│── users/                # App for authentication & profiles
│── templates/            # HTML templates
│── static/               # CSS, JS, Bootstrap files
│── manage.py             # Django management script

Deployment

Deploy on AWS EC2, PythonAnywhere, or any preferred cloud platform.

Update allowed hosts and database settings in settings.py.

Evaluation Criteria

Django best practices in backend development.

Usability and responsiveness of frontend.

Code quality and structure.

Use of MySQL & deployment.

Creativity and problem-solving skills.

Author: [Mahvish Ruhi]
GitHub Repo: [https://github.com/Mahvish16/Travel-Booking]
Live Demo: [https://mahvish.pythonanywhere.com/]
