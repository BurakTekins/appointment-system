from django.urls import path 
from users import views
<<<<<<< HEAD
from reservations.views import admin_page_view

urlpatterns = [
    path('sign_in/',views.sign_in_view,name= "sign_in"),
    path('sign_up/',views.sign_up_view,name= "sign_up"),
    path('logout/', views.logout_view, name='logout'), 
    path('admin_panel/',admin_page_view, name='admin_page'), ]
=======

urlpatterns = [
    path('sign_in/',views.sign_in_view,name= "sign_in"),
    path('sign_up/',views.sign_up_view,name= "sign_up"), ]

>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
