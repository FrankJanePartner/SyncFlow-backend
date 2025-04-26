from django.urls import path
from .views import home, dashboard, add_brand, add_social

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-brand/', add_brand, name='add-brand'),
    path('add-social/', add_social, name='add-social'),
]
