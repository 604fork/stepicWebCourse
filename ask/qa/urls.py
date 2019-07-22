import views

urlpatterns = patterns ('qa.views',
    url(r'^$', test, name='test'),
    url(r'^login/$', test, name='test'),
    url(r'^signup/$', test, name='test'),
    url(r'^ask/$', test, name='test'),
    url(r'^popular/$', test, name='test'),
    url(r'^new/$', test, name='test'),
    url(r'^question/([0-9]{*})/$', test, name='test'),
)
