from .models import Brand

def associate_brand(backend, user, response, *args, **kwargs):
    request = backend.strategy.request
    brand_id = request.session.get("brand_id")
    if not brand_id:
        return

    try:
        brand = Brand.objects.get(id=brand_id, owner=user)
        social = kwargs.get("social")
        if social:
            # link account to brand
            from .models import SocialAccount
            SocialAccount.objects.update_or_create(
                brand=brand,
                provider=backend.name,
                uid=social.uid,
                defaults={
                    "access_token": social.extra_data.get("access_token"),
                    "extra_data": social.extra_data,
                }
            )
    except Brand.DoesNotExist:
        pass
