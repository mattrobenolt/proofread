from django.conf.urls import patterns, url
from django.http import HttpResponse


def ok(request):
    return HttpResponse()


urlpatterns = patterns('',
    url(r'^$', ok),
    url(r'^thisisawesome/', ok)
)
