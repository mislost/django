from django.conf.urls import patterns,include,url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns=patterns('',
#Examples:
#url(r'^$','website.views.home',name='home'),
#url(r'^blog/',include('blog.urls')),

url(r'^admin/',include(admin.site.urls)),
url(r'^$','client.views.index'),
url(r'test.html','client.views.test'),
url(r'server.html','client.views.Servers'),
url(r'data.html','client.views.Datatables'),
url(r'ajax.html','client.views.Ajax'),
url(r'^accounts/login.*','django.contrib.auth.views.login',{'template_name':'login2.html'}),
url(r'login','client.views.user_login'),
url(r'acl.html','client.views.acl'),
url(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_DIR})

)

