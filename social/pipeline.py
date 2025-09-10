from core.models import Brand
from .models import SocialAccount

def bind_brand(strategy, backend, user, social=None, *args, **kwargs):
    """
    Attach social account to a Brand if brand_id was passed in the request.
    """
    brand_id = strategy.session_get("brand_id")  # pulled from session/query param
    if brand_id and social:
        try:
            brand = Brand.objects.get(id=brand_id, owner=user)
            SocialAccount.objects.get_or_create(
                brand=brand,
                user_social_auth=social
            )
        except Brand.DoesNotExist:
            pass
