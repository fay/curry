from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('{{ app_name }}.views',
    url(r'^$', "index", name='{{app_name}}_index'),
)
