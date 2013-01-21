from django.conf.urls import patterns, url
from django.http import HttpResponse


def ok(request):
    return HttpResponse()


def post(request):
    if request.method == 'GET':
        return HttpResponse(status=405)
    # This is supposed to fail if 'a' wasn't posted
    return HttpResponse(request.POST['a'])


urlpatterns = patterns('',
    url(r'^$', ok),
    url(r'^thisisawesome/', ok),
    url(r'^post/', post),
)
