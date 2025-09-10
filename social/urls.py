from django.urls import path
from .views import (
    SocialAuthInitView,
    SocialAuthCallbackView,
    SocialAccountListCreateView,
    SocialAccountRetrieveUpdateDestroyView,
    social_init_with_brand
)

urlpatterns = [
    # path('auth/<str:platform>/init/', SocialAuthInitView.as_view(), name='social-auth-init'),
    path('auth/callback/', SocialAuthCallbackView.as_view(), name='social-auth-callback'),
    path('accounts/', SocialAccountListCreateView.as_view(), name='social-account-list'),
    path('accounts/<int:pk>/', SocialAccountRetrieveUpdateDestroyView.as_view(), name='social-account-detail'),
    path("auth/<str:provider>/init/", social_init_with_brand, name="social-init-with-brand"),
]
