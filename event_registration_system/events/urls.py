from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/book/', views.book_event, name='book_event'),
]
