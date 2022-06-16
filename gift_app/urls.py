from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipients/', views.recipients, name='recipients'),
    path('recipients/add', views.recipient_add, name='recipient_add'),
    path('recipients/<int:pk>/edit', views.recipient_edit,
         name='recipient_edit'),
    path('recipient_list', views.recipient_list, name='recipient_list'),
    path('occasions/', views.occasions, name='occasions'),
    path('occasion_list', views.occasion_list, name='occasion_list'),
    path('occasion/add', views.occasion_add, name='occasion_add'),
    path('occasion/<int:pk>/edit', views.occasion_edit,
         name='occasion_edit'),
    path('gifts/', views.gifts, name='gifts'),
    path('gifts/add', views.gift_add, name='gift_add'),
    path('gift_list', views.gift_list, name='gift_list'),
    path('gifts/<int:pk>/view', views.gift_view, name='gift_view'),
    path('gifts/<int:pk>/edit', views.gift_edit, name='gift_edit'),
]
