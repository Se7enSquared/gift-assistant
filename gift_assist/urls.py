from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', include('gift_app.urls')),
    path('gift-backend/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
