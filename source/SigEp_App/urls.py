from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SigEp_App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^index.html', 'home.views.index'),
    url(r'^bms.html', 'home.views.bms'),
    url(r'^contact.html', 'home.views.contact')
)
