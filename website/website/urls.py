from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'client.views.index'),
    url(r'test.html', 'client.views.test'),
    url(r'data.html', 'client.views.Datatables'),
    url(r'ajax.html','client.views.Ajax'),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.CSS_DIR})
    
)
