from django.urls import path
from . import views

urlpatterns = [
    path('', views.autoproduct_list, name='autoproduct_list'), #список запчастей
    path('create/', views.autoproduct_create, name='autoproduct_create'),
    path('edit/<int:pk>/', views.autoproduct_edit, name='autoproduct_edit'),
    path('delete/<int:pk>/', views.autoproduct_delete, name='autoproduct_delete'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/create/', views.store_create, name='store_create'),
    path('stores/edit/<int:pk>/', views.store_edit, name='store_edit'),
    path('stores/delete/<int:pk>/', views.store_delete, name='store_delete'),
]
