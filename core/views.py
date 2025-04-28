from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Brand, BrandSocialAccount
from allauth.socialaccount.providers import registry


# Create your views here.
def home(request):
    user = request.user
    
    if user.is_authenticated:
        return redirect("core:dashboard")
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    providers = registry.get_class_list()
    provider_list = [{'id': provider.id, 'name': provider.name} for provider in providers]
    context = {'providers': provider_list}
    return render(request, 'core/dashboard.html', context)

@login_required
def add_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.POST.get('logo')

    Brand.objects.get_or_create(
        user = request.user,
        name = name,
        logo = image,
        description = description
    )

    messages.success(request, 'Brand added Successfully')
    return redirect('core:dashboard')


# @login_required
# def add_social(request):
#     if request.method == 'POST':
#         brand_id = request.POST.get('brand_id')
#         provider = request.POST.get('provider')
#         access_token = request.POST.get('access_token')

#     brand = get_object_or_404(Brand, id=brand_id, owner=request.user)

#     BrandSocialAccount.objects.get_or_create(
#         brand=brand,
#         provider=provider,
#         uid=provider_user_id,
#         access_token=access_token,
#         extra_data=social_data
#     )
    
#     return redirect('/accounts/facebook/login/')


@login_required
def add_social(request):
    if request.method == 'POST':
        brand_id = request.POST.get('brand_id')
        provider = request.POST.get('provider')

        # Save brand in session for use after callback
        request.session['selected_brand_id'] = brand_id

        # Redirect to provider login using allauth
        return redirect(f'/accounts/{provider}/login/')

