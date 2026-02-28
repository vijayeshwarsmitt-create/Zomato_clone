from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
]
