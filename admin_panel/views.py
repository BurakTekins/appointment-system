from django.shortcuts import render, redirect
from reservations.models import Reservation
from announcements.models import Announcement 
from announcements.forms import AnnouncementForm
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import date
from django.http import JsonResponse
from django.utils.timezone import now

def staff_required(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(staff_required)
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_announcement')
    else:
        form = AnnouncementForm()
    return render(request, 'admin_panel/create_announcement.html', {'form': form})

@login_required
def todays_reservations(request):
    today = date.today()
    reservations = Reservation.objects.filter(date=today).select_related('user')
    return render(request, 'admin_panel/todays_reservations.html', {'reservations': reservations})

def get_active_reservation_user(request):
    current_time = now().time()
    today = date.today()
    active_reservation = Reservation.objects.filter(
        date=today,
        start_time__lte=current_time,
        end_time__gte=current_time
    ).select_related('user').first()
    if active_reservation:
        user = active_reservation.user
        name = user.get_full_name() or user.username
        return JsonResponse({'name': name})
    return JsonResponse({'name': None})
