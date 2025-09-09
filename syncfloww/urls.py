from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView


# from syncflowbackend.UserAccount import views

admin.site.site_header = 'SyncFloww'
admin.site.site_title = 'SyncFloww Admin Panel'
admin.site.index_title = 'SyncFloww Administration'




urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication and user management
    path('api/auth/', include('UserAccount.urls', namespace='accounts')),
    path("api/social_auth/", include('social_django.urls', namespace="social_auth")),  
    
    # Analytics
    path('api/analytics/', include('analytics.urls')),
    
    # Automations
    path('api/automations/', include('automations.urls')),
    
    # Campaigns
    path('api/campaigns/', include('campaigns.urls')),

   # core
    path('api/', include('core.urls')),
    path('', RedirectView.as_view(url='/api/guest'), name='root_redirect'),

    
    # Integrations
    path('api/integrations/', include('integrations.urls')),

    # socials
    path('api/social/', include('social.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #Favicon path
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
]

# static files (when using runserver with --insecure)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if hasattr(settings, 'STATICFILES_DIRS') and settings.STATICFILES_DIRS:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
