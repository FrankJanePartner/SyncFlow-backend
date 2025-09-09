from django.urls import path
from .views import BrandListCreateView, BrandDetailView, guest_demo

urlpatterns = [
    path('brands/', BrandListCreateView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('guest', guest_demo, name="guest")
]
