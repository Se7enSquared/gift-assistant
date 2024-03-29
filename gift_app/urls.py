from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate_age/<int:year>/<int:month>/<int:day>', views.calculate_age, name='calculate_age'),
    path('calculate_birth_year/<int:age>/<int:month>/<int:day>', views.calculate_birth_year, name='calculate_birth_year'),
    path('recipients/', views.recipients, name='recipients'),
    path('recipients/add', views.recipient_add, name='recipient_add'),
    path('recipient_list', views.recipient_list, name='recipient_list'),
    path('recipients/<int:pk>/edit', views.recipient_edit,
         name='recipient_edit'),
    path('recipients/<int:pk>/delete', views.recipient_delete,
         name='recipient_delete'),
    path('occasions/', views.occasions, name='occasions'),
    path('occasion_list', views.occasion_list, name='occasion_list'),
    path('occasion/add', views.occasion_add, name='occasion_add'),
    path('occasion/<int:pk>/edit', views.occasion_edit,
         name='occasion_edit'),
    path('occasions/<int:pk>/delete', views.occasion_delete,
         name='occasion_delete'),
    path('gifts/', views.gifts, name='gifts'),
    path('gifts/add', views.gift_add, name='gift_add'),
    path('gift_list', views.gift_list, name='gift_list'),
    path('gifts/<int:pk>/edit', views.gift_edit, name='gift_edit'),
    path('gifts/<int:pk>/delete', views.gift_delete, name='gift_delete'),
]
