from django.urls import path
from . import views
<<<<<<< HEAD
from users.views import update_user , delete_user 

urlpatterns = [
    path('<int:user_id>/', views.user_reservation_page, name='user_reservation'),  
    path('<int:user_id>/user_info/', update_user, name='user_info'), 
    path('user/delete/<int:user_id>/', delete_user, name='delete_user'), 
=======
from users.views import update_user 

urlpatterns = [
    path('<int:user_id>/', views.user_reservation_page, name='user_reservation'),  
    path('<int:user_id>/user_info/', update_user, name='user_info'),  
>>>>>>> ca6f786d3743ba4893ef7ccda14fe98137f5bca3
    path('create/', views.create_reservation, name='create_reservation'),
    path('my-reservations/', views.my_reservations_view, name='my_reservations'),
]
