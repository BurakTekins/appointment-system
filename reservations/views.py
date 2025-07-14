<<<<<<< HEAD

=======
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth import get_user_model
from .models import Reservation
from django.contrib import messages
from users import models
from users import forms
from datetime import datetime , timedelta , time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

def get_next_4_days_excluding_sundays():
    today = datetime.today().date()
    day = today + timedelta(days=1)
    result = []
    while len(result) < 4:
        if day.weekday() != 6:
            result.append(day)
        day += timedelta(days=1)
    return result

=======

User = get_user_model()

>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
def user_reservation_page(request, user_id):
    user = get_object_or_404(User, id=user_id)
    selected_date = None
    duration = None
    available_slots = []
<<<<<<< HEAD
    conflict_msg = None
    available_days = get_next_4_days_excluding_sundays()
=======
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

    if request.method == 'GET':
        duration = request.GET.get('duration')
        selected_date = request.GET.get('date')

        if duration and selected_date:
            duration = int(duration)
<<<<<<< HEAD
            try:
                selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
            except ValueError:
                try:
                    selected_date = datetime.strptime(selected_date.split("T")[0], "%Y-%m-%d").date()
                except ValueError:
                    try:
                        selected_date = datetime.strptime(selected_date, "%B %d, %Y").date()
                    except Exception:
                        selected_date = None

            if selected_date:
                if Reservation.objects.filter(user=user, date=selected_date).exists():
                    conflict_msg = "Bu tarihte zaten bir rezervasyonunuz var."
                else:
                    reservations = Reservation.objects.filter(date=selected_date)
                    available_slots = generate_all_slots_with_status(selected_date, duration, reservations)
=======
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

            if Reservation.objects.filter(user=user, date=selected_date).exists():
                conflict_msg = "Bu tarihte zaten bir rezervasyonunuz var."
            else:
                reservations = Reservation.objects.filter(date=selected_date)
                available_slots = generate_available_slots(selected_date, duration, reservations)
                conflict_msg = None
        else:
            conflict_msg = None
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

    return render(request, 'reservations/reservation_page.html', {
        'user': user,
        'available_slots': available_slots,
        'selected_date': selected_date,
        'duration': duration,
<<<<<<< HEAD
        'conflict_msg': conflict_msg,
        'available_days': available_days
    })

@staff_member_required
def admin_page_view(request):
    user = request.user
    selected_date = None
    duration = None
    available_slots = []
    conflict_msg = None
    available_days = get_next_4_days_excluding_sundays()

    if request.method == 'GET':
        duration = request.GET.get('duration')
        selected_date = request.GET.get('date')

        if duration and selected_date:
            duration = int(duration)
            try:
                selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
            except ValueError:
                try:
                    selected_date = datetime.strptime(selected_date.split("T")[0], "%Y-%m-%d").date()
                except ValueError:
                    try:
                        selected_date = datetime.strptime(selected_date, "%B %d, %Y").date()
                    except Exception:
                        selected_date = None

            if selected_date:
                reservations = Reservation.objects.filter(date=selected_date)
                available_slots = generate_all_slots_with_status(selected_date, duration, reservations)

    return render(request, 'users/admin_page.html', {
        'user': user,
        'available_slots': available_slots,
        'selected_date': selected_date,
        'duration': duration,
        'conflict_msg': conflict_msg,
        'available_days': available_days
    })



def generate_all_slots_with_status(date, duration, reservations):
=======
        'conflict_msg': conflict_msg
    })


def generate_available_slots(date, duration, reservations):
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
    opening = time(10, 0)
    closing = time(20, 0)
    slots = []
    dt = datetime.combine(date, opening)

    while dt.time() < closing:
        end_time = (dt + timedelta(hours=duration)).time()
        if end_time > closing:
            break

        conflict = any(
            res.start_time < end_time and res.end_time > dt.time()
            for res in reservations
        )

<<<<<<< HEAD
        slots.append({
            'start': dt.time(),
            'end': end_time,
            'is_available': not conflict
        })
=======
        if not conflict:
            slots.append((dt.time(), end_time))
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

        dt += timedelta(minutes=30)

    return slots

<<<<<<< HEAD
from django.utils.timezone import now

@login_required(login_url='sign_in')
def my_reservations_view(request):
    all_reservations = Reservation.objects.filter(user=request.user).order_by('date', 'start_time')

    upcoming_reservations = all_reservations.filter(date__gte=now().date())
    past_reservations = all_reservations.filter(date__lt=now().date())

    return render(request, 'reservations/my_reservations.html', {
        'upcoming_reservations': upcoming_reservations,
        'past_reservations': past_reservations,
    })

@login_required(login_url='sign_in')
def create_reservation(request):
    if request.method == 'POST':
        user = request.user

        date_str = request.POST.get('date')
        start_str = request.POST.get('start_time')
        end_str = request.POST.get('end_time')

        if not date_str or not start_str or not end_str:
            messages.error(request, "Tüm alanlar gereklidir.")
            return redirect('user_reservation', user_id=user.id)

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            try:
                date = datetime.strptime(date_str.split("T")[0], "%Y-%m-%d").date()
            except ValueError:
                try:
                    date = datetime.strptime(date_str, "%B %d, %Y").date()
                except Exception:
                    messages.error(request, f"Tarih formatı desteklenmiyor: {date_str}")
                    return redirect('user_reservation', user_id=user.id)

        try:
            try:
                start_time = datetime.strptime(start_str, "%H:%M:%S").time()
            except ValueError:
                start_time = datetime.strptime(start_str, "%H:%M").time()

            try:
                end_time = datetime.strptime(end_str, "%H:%M:%S").time()
            except ValueError:
                end_time = datetime.strptime(end_str, "%H:%M").time()

        except ValueError:
            messages.error(request, "Saat formatı geçersiz.")
            return redirect('user_reservation', user_id=user.id)

        if Reservation.objects.filter(user=user, date=date).exists():
            messages.error(request, "Bu tarihte zaten bir rezervasyonunuz var.")
=======

def create_reservation(request):
    if request.method == 'POST':
        user = request.user
        date_str = request.POST.get('date')          
        start_str = request.POST.get('start_time')   
        end_str = request.POST.get('end_time')       

       
        try:
            date = datetime.strptime(date_str, "%B %d, %Y").date()
            start_time = datetime.strptime(start_str, "%I:%M %p").time()
            end_time = datetime.strptime(end_str, "%I:%M %p").time()
        except ValueError:
            messages.error(request, "Tarih veya saat formatı geçersiz. Lütfen tekrar deneyin.")
            return redirect('user_reservation', user_id=user.id)

        if Reservation.objects.filter(user=user, date=date).exists():
            messages.error(request, "Aynı gün içinde sadece bir rezervasyon yapılabilir.")
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
            return redirect('user_reservation', user_id=user.id)

        Reservation.objects.create(
            user=user,
            date=date,
            start_time=start_time,
            end_time=end_time
        )
        messages.success(request, "Rezervasyon başarıyla oluşturuldu.")
        return redirect('user_reservation', user_id=user.id)

<<<<<<< HEAD
    else:
        messages.error(request, "Geçersiz istek.")
        return redirect('home_page')


from django.utils.timezone import now

def get_active_reservation_user(reservations):
    current_time = now().time()
    for r in reservations:
        if r.start_time <= current_time and r.end_time > current_time:
            return r.user.name
    return None
=======
    

def my_reservations_view(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-start_time')
    return render(request, 'reservations/my_reservations.html', {
        'reservations': reservations
    })

>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3

    
