from django.db import models
from django.contrib.auth.models import User

TravelTypes=[
    ('Flight', 'Flight'),
    ('Train', 'Train'),
    ('Bus', 'Bus')
]

Status=[
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled')
]

class Travel (models.Model):
    type = models.CharField(max_length=10, choices=TravelTypes)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avaliable_seats = models.IntegerField()

    def __str__(self):
        return self.type

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(Travel, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateField()
    status = models.CharField(max_length=10, choices=Status)

    def __str__(self):
        return self.Travel_option



