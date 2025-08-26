from __future__ import annotations
from typing import Any, Optional, TypeVar
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from allauth.account.models import EmailAddress
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from typing import Any

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self,
        username: Any = None,   # kept for compatibility, not used
        email: str | None = None,
        password: str | None = None,
        **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: Any = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    # 👇 correct annotation makes Pyright/mypy happy
    objects: CustomUserManager = CustomUserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
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
    class Meta:
        proxy = True
        verbose_name = "Email Address"
        verbose_name_plural = "Email Addresses"
        app_label = "accounts"

