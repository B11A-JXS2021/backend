from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registrations/', include('rest_auth.registration.urls')),
    path('sms/', include('sms.urls')),
    path('users/', include('users.urls')),
    path('drives/', include('drives.urls')),
]
