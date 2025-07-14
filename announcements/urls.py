from django.urls import path
from .views import homepage_view, announcement_list
from django.shortcuts import redirect

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('duyurular/', announcement_list, name='announcement_list'),
    path('duyuru_oluştur', lambda request: redirect('create_announcement'), name='duyuru_redirect'),
]


