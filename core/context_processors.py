from .models import Brand, BrandSocialAccount


def brand(request):
    brands = Brand.objects.filter(user=request.user) if request.user.is_authenticated else []
    
    context = {
        'brands': brands,
    }
    return context
