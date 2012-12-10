#from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
#from django.core.urlresolvers import reverse
#from django.shortcuts import redirect

from views import MessagesView


urlpatterns = patterns('ndb.simple_messages.views',
    url(r'^$', MessagesView.as_view(),  name='simple_messages'),
)
