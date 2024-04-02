from django.urls import path
from .apis import *

urlpatterns = [
    path('floors/', FloorList.as_view(), name='floor-list'),
    path('floors/<int:pk>/', FloorDetail.as_view(), name='floor-detail'),
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('buildings/', BuildingList.as_view(), name='buildings-list'),
    path('buildings/<int:pk>/', BuildingDetail.as_view(), name='buildings-detail'),

]
