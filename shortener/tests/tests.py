import pytest
from django.urls import reverse
from django.test import Client

from shortener.cron import delete_unused_aliases
from shortener.models import Url
from shortener.services import alias_generator


@pytest.mark.django_db
def test_url_shortening_view(url):
    path = reverse('url_short')
    response_get = Client().get(path)
    response_post = Client().post(path, {'url': url.url})
    assert response_get.status_code == 200
    assert response_post.status_code == 200


@pytest.mark.django_db
def test_alias_click_view(url):
    alias = url.alias
    path = reverse('click', kwargs={'alias': alias})
    response = Client().get(path)
    assert response.status_code == 302
    assert len(Url.objects.filter(last_visit=None)) == 0


@pytest.mark.django_db
def test_alias_generator():
    alias = alias_generator()
    digits = [x for x in alias if x.isnumeric()]
    letters = [y for y in alias if y not in digits]
    assert type(alias) == str
    assert len(alias) == 10
    assert int(digits[-1]) == len(letters)


@pytest.mark.django_db
def test_alias_click_view_exception(url):
    alias = url.alias[::-1]
    path = reverse('click', kwargs={'alias': alias})
    response = Client().get(path)
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_unused_aliases(urls, visited_urls):
    delete_unused_aliases()
    assert len(Url.objects.filter(last_visit=None)) == 2
    assert len(Url.objects.all()) == 4
