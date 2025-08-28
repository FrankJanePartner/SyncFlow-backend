from __future__ import annotations
from typing import Any, Optional, TypeVar
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    company = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    timezone = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.email}'s profile"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class EmailAddressProxy(EmailAddress):
    class Meta:  # type: ignore[override]
        proxy = True
        verbose_name = "Email Address"
        verbose_name_plural = "Email Addresses"
        app_label = "accounts"
