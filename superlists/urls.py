from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
   # Examples:
   # url(r'^blog/', include('blog.urls')),
   # url(r'^admin/', include(admin.site.urls)),
            url(r'^$', 'lists.views.home_page', name='home'),
            url(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'), # (.+) will capture anything
            url(r'^lists/(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
            url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
            # between / / in the URL, and send it as an argument to the view.

)
