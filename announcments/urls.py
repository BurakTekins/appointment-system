from django.urls import path
from .views import homepage_view, announcement_list

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('duyurular/', announcement_list, name='announcement_list'),
]


