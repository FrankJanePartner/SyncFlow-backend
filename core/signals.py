from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from .models import Brand, BrandSocialAccount

@receiver(social_account_added)
def link_social_to_brand(request, sociallogin, **kwargs):
    user = request.user
    brand_id = request.session.get('selected_brand_id')

    if brand_id:
        try:
            brand = Brand.objects.get(id=brand_id, user=user)

            BrandSocialAccount.objects.get_or_create(
                brand=brand,
                provider=sociallogin.account.provider,
                uid=sociallogin.account.uid,
                access_token=sociallogin.token.token,
                refresh_token=sociallogin.token.token_secret,
                extra_data=sociallogin.account.extra_data,
            )

            # Clean up session
            del request.session['selected_brand_id']
        except Brand.DoesNotExist:
            pass
