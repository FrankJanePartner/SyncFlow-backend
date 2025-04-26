from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Brand, BrandSocialAccount

# Create your views here.
def home(request):
    user = request.user
    
    if user.is_authenticated:
        return redirect("core:dashboard")
    return render(request, 'core/home.html')


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

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


@login_required
def add_social(request):
    if request.method == 'POST':
        provider = request.POST.get('provider')

    # BrandSocialAccount.objects.get_or_create(
    #     brand = request.user,
    #     provider = name,
    #     uid = image,
    #     description = description
    # )

    # messages.success(request, 'added Successfully')
    return redirect('core:dashboard')
