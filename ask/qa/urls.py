from qa.views import test
from django.conf.urls import url

urlpatterns = [ 
    url(r'^$', test, name='qa.views.test'),
    url(r'^login/$', test, name='qa.views.test'),
    url(r'^signup/$', test, name='qa.views.test'),
    url(r'^ask/$', test, name='qa.views.test'),
    url(r'^popular/$', test, name='qa.views.test'),
    url(r'^new/$', test, name='qa.views.test'),
    url(r'^question/\d+/$', test, name='qa.views.test'),
]
