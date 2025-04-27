from django.db import models
from django.conf import settings

# Create your models here.
class Brand(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to="Brand_logo/", blank=True, default="default/brand_default")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class BrandSocialAccount(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='social_accounts')
    provider = models.CharField(max_length=50)  # e.g., 'google', 'facebook'
    uid = models.CharField(max_length=255)  # user id from the provider
    access_token = models.TextField()
    refresh_token = models.TextField(blank=True, null=True)
    token_expires = models.DateTimeField(blank=True, null=True)
    extra_data = models.JSONField(default=dict)
    connected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['brand', 'provider', 'uid']
        verbose_name = 'Brand Social Account'
        verbose_name_plural = 'Brand Social Accounts'


    def __str__(self):
        return self.provider

