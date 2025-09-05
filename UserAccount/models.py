from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str = None,
        first_name: str = "",
        last_name: str = "",
        is_staff=False,
        is_superuser=False,
        **extra_fields,
    ) -> "User":
        if not email:
            raise ValueError("User must have an email")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name or "",
            last_name=last_name or "",
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, first_name="Admin", last_name="User", **extra_fields) -> "User":
        return self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None  # disable username field

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # don’t require first/last name for createsuperuser
