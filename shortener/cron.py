from shortener.models import Url
from django.utils import timezone


def delete_unused_aliases():
    expiration_datetime = timezone.now() - timezone.timedelta(days=2)
    for alias in Url.objects.filter(last_visit=None, date_created__lt=expiration_datetime):
        alias.delete()
    for alias in Url.objects.filter(last_visit__lt=expiration_datetime):
        alias.delete()
    return True
