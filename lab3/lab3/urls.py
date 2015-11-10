from django.conf.urls import patterns, include, url
from blog.views import showrecord,search,delete,click_result
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab3.views.home', name='home'),
    # url(r'^lab3/', include('lab3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    #('^hello/$',hello),
    #('^time/$',current_datetime),
    (r'^showifm/$', showrecord),
    (r'^search/$', search),
    (r'^delete/$', delete),
    (r'^click_result/$', click_result),
    
    
)
