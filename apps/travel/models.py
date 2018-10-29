from __future__ import unicode_literals
from django.db import models
from ..LogReg.models import User
from datetime import datetime

class TripManager(models.Manager):
    def check_trip(self, data, user):
        errors = []
        today = datetime.now().date()
        start = datetime.strptime(data['travel_start_date'], '%Y-%m-%d').date()
        end = datetime.strptime(data['travel_end_date'], '%Y-%m-%d').date()
        if len(data['destination']) < 1 or len(data['plan']) < 1 or len(data['travel_start_date']) < 1 or len(data['travel_end_date']) < 1:
            errors.append(['destination and plan', 'All fields must be entered.'])
        #validate dates are future
        if start < today or end < today:
            errors.append(['date', 'Traveling dates must be in the future.'])
        # #validate date to not before date from
        if end < start:
            errors.append(['date', 'End date must be later than start date.'])

        if errors:
            return [False, errors]
        else:
            newTrip = Trip.objects.create(destination=data['destination'], plan=data['plan'], planner=user, travel_start_date=data['travel_start_date'],  travel_end_date=data['travel_end_date'])
            newTrip.travelers.add(user)
            newTrip.save()
            return [True]
# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    plan = models.TextField()
    planner = models.ForeignKey(User, related_name='trip_planner')
    travelers = models.ManyToManyField(User, related_name='trip_travelers')
    travel_start_date = models.DateTimeField()
    travel_end_date = models.DateTimeField()
    objects = TripManager()
