from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/',views.ProfileList.as_view(), name='profile-list'),
    path('profile/<int:pk>/',views.ProfileDetail.as_view(), name='profile-details')
]