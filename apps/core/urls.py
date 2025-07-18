from django.urls import path
from .views import BrandListCreateView, BrandDetailView

urlpatterns = [
    path('brands/', BrandListCreateView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
]
