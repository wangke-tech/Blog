from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT }),  
    url(r'^$','article.views.home',name = 'home'),
    url(r'^edit/', include(admin.site.urls)),
    url(r'^current_time/$','article.views.test'),
    url(r'^details/(?P<id>\d+)/$','article.views.details',name = 'details'),
)
