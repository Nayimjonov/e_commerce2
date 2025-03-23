from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.OrderListCreateAPIView.as_view(), name='list'),
    path('orders/<int:pk>/', views.OrderDetailAPIView.as_view(), name='detail'),
]