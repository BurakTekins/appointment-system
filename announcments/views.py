from django.shortcuts import render
from .models import Announcments

def homepage_view(request):
    latest_announcements = Announcments.objects.order_by('-created')[:3]
    return render(request, 'base.html', {'latest_announcements': latest_announcements})

def announcement_list(request):
    all_announcements = Announcments.objects.order_by('-created')
    return render(request, 'announcments/announcement_list.html', {'announcements': all_announcements})
