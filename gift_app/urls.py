from django.urls import path

from . import views

urlpatterns = [
    path('recipients/', views.recipient_list, name='recipients'),

]
