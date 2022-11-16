import pytest
from shortener.models import Url
from django.utils import timezone


@pytest.fixture
def url():
    url = Url.objects.create(
        url='https://www.example.com/search?channel=fs&client=ubuntu&q=zabawne+koty',
        alias='a1234aaaa5',
        )
    return url


@pytest.fixture
def urls():
    urls = []
    for x in range(5):
        url = Url.objects.create(
            url=f'https://www.example.com/search?channel=fs&client=ubuntu&q=zabawne+koty{x}',
            alias=f'a1234aaaa{x}',
            )
        urls.append(url)
    for url in urls:
        url.date_created = timezone.now() - timezone.timedelta(days=urls.index(url))
        url.save()
    return urls


@pytest.fixture
def visited_urls():
    visited_urls = []
    for x in range(5):
        url = Url.objects.create(
            url=f'https://www.example.com/search?channel=fs&client=ubuntu&q=zabawne+koty{x}',
            alias=f'b1234aaaa{x}',
            last_visit=timezone.now() - timezone.timedelta(days=x)
            )
        visited_urls.append(url)
    return visited_urls
