from django.urls import path, include
from users import views


urlpatterns = [
    path('userinfos/', views.UserInfo.as_view(), name="user_info"),
]
