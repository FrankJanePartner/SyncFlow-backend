from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


admin.site.site_header = 'SyncFlow'
admin.site.site_title = 'SyncFlow Admin Panel'
admin.site.index_title = 'SyncFlow Administration'

urlpatterns = [
    path('admin/', admin.site.urls),

    # my apps urls
    path('', include('core.urls', namespace='core')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),

    # third party urls
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

