from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        unique_together = ('event', 'user')  # Ensure a user can book only once per event

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
