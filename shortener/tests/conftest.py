import pytest
from shortener.models import Url


@pytest.fixture
def url():
    url = Url.objects.create(
        url='https://www.example.com/search?channel=fs&client=ubuntu&q=zabawne+koty',
        alias='a1234aaaa5',
        )
    return url
