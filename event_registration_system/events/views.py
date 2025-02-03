from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Booking
from django.contrib import messages
from django.utils.timezone import now

def homepage(request):
    return render(request, 'events/homepage.html')

def event_list(request):
    events = Event.objects.filter(date__gte=now())
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def create_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        max_participants = request.POST['max_participants']
        Event.objects.create(
            name=name, date=date, max_participants=max_participants, created_by=request.user
        )
        messages.success(request, "Event created successfully!")
        return redirect('event_list')
    return render(request, 'events/create_event.html')

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        if Booking.objects.filter(event=event, user=request.user).exists():
            messages.error(request, "You have already booked a seat for this event!")
        elif Booking.objects.filter(event=event).count() >= event.max_participants:
            messages.error(request, "No seats available for this event!")
        else:
            email = request.POST['email']
            Booking.objects.create(event=event, user=request.user, email=email)
            messages.success(request, "Successfully booked a seat!")
        return redirect('event_list')
    return render(request, 'events/book_event.html', {'event': event})
