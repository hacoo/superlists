from django.conf.urls import patterns, url

urlpatterns = patterns('',
            url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'), # (.+) will capture anything
            url(r'^new$', 'lists.views.new_list', name='new_list'),
            # between / / in the URL, and send it as an argument to the view.

)
