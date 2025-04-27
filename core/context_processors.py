from .models import Brand, BrandSocialAccount
from allauth.socialaccount.providers import registry


def brand(request):
    brands = Brand.objects.filter(user=request.user) if request.user.is_authenticated else []
    
    context = {
        'brands': brands,
    }
    return context


def enabled_social_providers(request):
    providers = registry.get_class_list()
    provider_list = [{'id': provider.id, 'name': provider.name} for provider in providers]
    return {'providers': provider_list}
