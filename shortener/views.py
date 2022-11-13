from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View
from shortener.forms import UrlShortenerForm
from shortener.models import Url
from django.utils import timezone
from shortener.services import alias_generator


class UrlShorteningView(View):

    def get(self, request):
        return render(request, 'form.html', {'form': UrlShortenerForm()})

    def post(self, request):
        form = UrlShortenerForm(request.POST)
        alias = None
        if form.is_valid():
            url = form.cleaned_data['url']
            alias = alias_generator()
            Url.objects.create(url=url, alias=alias)
        return render(request, 'form.html', {'form': form, 'alias': alias})


class AliasClickView(View):
    def get(self, request, alias):
        try:
            clicked_url = Url.objects.get(alias=alias)
            clicked_url.last_visit = timezone.now()
            clicked_url.save()
            return HttpResponseRedirect(clicked_url.url)
        except ObjectDoesNotExist:
            raise Http404(f'{alias} does not exist or has been expired')
