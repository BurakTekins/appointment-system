from django.shortcuts import render, redirect
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib import messages

def homepage_view(request):
    latest_announcements = Announcement.objects.order_by('-created')[:3]
    return render(request, 'base.html', {'latest_announcements': latest_announcements})

def announcement_list(request):
    all_announcements = Announcement.objects.order_by('-created')
    return render(request, 'announcements/announcement_list.html', {'announcements': all_announcements})
