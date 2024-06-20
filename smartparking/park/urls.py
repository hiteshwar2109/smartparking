from django.urls import path
from .views import  register_view, index, login_view, home_view, reservation_view, reserve_slot, user, details, downtown,airport,mall,stadium,office

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
     path('user/', user, name='user'),
    path('', index, name='index'),
    path('reservation_view/', reservation_view, name='reservation_view'),
    path('reserve/', reserve_slot, name='reserve_slot'),
    path('home/downtown/details/', details, name='details'),
    path('home/downtown/', downtown, name='downtown'),
    path('home/airport/details/', details, name='details'),
    path('home/airport/', airport, name='airport'),
    path('home/mall/details/', details, name='details'),
    path('home/mall/',mall, name='mall'),
    path('home/stadium/details/', details, name='details'),
    path('home/stadium/',stadium, name='stadium'),
    path('home/office/details/', details, name='details'),
    path('home/office/',office, name='office'),
    
]

