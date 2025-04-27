# Create a file like: your_app/management/commands/sync_socialapps.py

from django.core.management.base import BaseCommand
from django.conf import settings
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = 'Sync SOCIALACCOUNT_PROVIDERS into SocialApp table'

    def handle(self, *args, **kwargs):
        site = Site.objects.get_current()

        for provider, config in settings.SOCIALACCOUNT_PROVIDERS.items():
            app_config = config.get('APP')
            if not app_config:
                self.stdout.write(self.style.WARNING(f"Skipping {provider}: No APP config found"))
                continue

            client_id = app_config.get('client_id')
            secret = app_config.get('secret')
            key = app_config.get('key', '')

            if not client_id or not secret:
                self.stdout.write(self.style.WARNING(f"Skipping {provider}: Missing client_id or secret"))
                continue

            app, created = SocialApp.objects.get_or_create(
                provider=provider,
                name=provider.capitalize(),
                defaults={
                    'client_id': client_id,
                    'secret': secret,
                    'key': key,
                }
            )

            if not created:
                app.client_id = client_id
                app.secret = secret
                app.key = key
                app.save()
                self.stdout.write(self.style.SUCCESS(f"Updated SocialApp: {provider}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Created SocialApp: {provider}"))

            # Ensure the app is connected to the current site
            if site not in app.sites.all():
                app.sites.add(site)
                self.stdout.write(self.style.SUCCESS(f"Connected {provider} to site {site.domain}"))
