from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^subscribers/', include('subscriber.urls')),
    #url(r'^hello/$', 'subscriber.views.hello'),
    #url(r'^hello_template/$', 'subscriber.views.hello_template'),
    #url(r'^hello_template_simple/$', 'subscriber.views.hello_template_simple'),
    url(r'^admin/', include(admin.site.urls)),

)
