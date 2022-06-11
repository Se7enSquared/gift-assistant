from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipients/', views.recipients, name='recipients'),
    path('gifts/', views.gift_list, name='gifts'),
    path('recipients/add', views.recipient_add, name='recipient_add'),
    path('recipients/<int:pk>/edit', views.recipient_edit,
         name='recipient_edit'),
    path('recipient_list', views.recipient_list, name='recipient_list'),
]
