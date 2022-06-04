from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('recipient.urls')),
    path('gift-backend/', admin.site.urls),
]
