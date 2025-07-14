
from django.urls import path
from . import views

urlpatterns = [
        path('get-active-user/', views.get_active_reservation_user, name='get_active_reservation_user'),
path('create_announcement/', views.create_announcement, name='create_announcement'),
    path('todays_reservations/', views.todays_reservations, name='todays_reservations'),
]
