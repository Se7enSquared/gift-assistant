from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipients/', views.recipient_list, name='recipients'),
    path('gifts/', views.gift_list, name='gifts'),
]
