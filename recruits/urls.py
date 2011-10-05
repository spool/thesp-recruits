from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$', 'recruits.views.recruit', name='recruit'),
    )
