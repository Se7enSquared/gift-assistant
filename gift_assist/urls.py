from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('gift_app.urls')),
    path('gift-backend/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
