from .models import Brand, BrandSocialAccount

def brand(request):
    brands = Brand.objects.filter(user=request.user)
    
    context = {
        'brands':brands,
    }
    return context