from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..LogReg.models import User
from .models import Trip

#displays main page with log and reg
def main(request):
    return render(request, 'travel/main.html')

#displays travel dashboard page
def dashboard(request):
    user = User.objects.get(id=request.session['user']['id'])
    context = {
        'trips': Trip.objects.filter(travelers=user),
        'other_trips': Trip.objects.all().exclude(travelers=user)
    }
    return render(request, 'travel/dashboard.html', context)

#adds other trip to user's trip
def join(request, id):
    user = User.objects.get(id=request.session['user']['id'])
    trip = Trip.objects.get(id=id)
    trip.travelers.add(user)
    trip.save()
    return redirect('travel:dashboard')

#displays destination page
def destination(request, id):
    context = {
        'trip': Trip.objects.get(id=id),
        'travelers': User.objects.filter(trip_travelers__id=id)
    }
    print (context['trip'].travel_start_date)
    return render(request, 'travel/destination.html', context)

#displays add page
def add_page(request):
    return render(request, 'travel/add.html')

#adds trip to user's trips
def add(request):
    if request.method == "POST":
        print (request.POST['travel_start_date'])
        user = User.objects.get(id=request.session['user']['id'])
        response = Trip.objects.check_trip(request.POST, user)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('travel:add_page')
    return redirect('travel:dashboard')

# Create your views here.
