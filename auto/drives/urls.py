from django.urls import path, include
from . import views



urlpatterns = [
    path('habit/', views.DriveData.as_view(), name="drive_data")
]
