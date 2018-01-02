from django.conf.urls import url

from . import invent

urlpatterns = [
    url(r'^$', invent.index, name='index'),
]
