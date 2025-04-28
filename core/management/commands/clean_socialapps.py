from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp

class Command(BaseCommand):
    help = 'Clean duplicate SocialApp entries for the same provider and site, keeping only one.'

    def handle(self, *args, **options):
        duplicates_found = False
        providers = SocialApp.objects.values_list('provider', flat=True).distinct()
        for provider in providers:
            apps = SocialApp.objects.filter(provider=provider).order_by('id')
            if apps.count() > 1:
                duplicates_found = True
                self.stdout.write(f"Found {apps.count()} SocialApp entries for provider '{provider}'. Keeping the first and deleting the rest.")
                # Keep the first app, delete the rest
                for app in apps[1:]:
                    self.stdout.write(f"Deleting SocialApp id={app.id} name={app.name}")
                    app.delete()
        if not duplicates_found:
            self.stdout.write("No duplicate SocialApp entries found.")
