from django.conf.urls import url, include
import django.contrib.auth.views
import tracker.views

urlpatterns = [
        url(r'^$', tracker.views.tracker_page, name='tracker-page'),
        url(r'^door-opener$', tracker.views.door_opener, name='door-opener'),
        url(r'^login$', django.contrib.auth.views.login, {'template_name': 'login.html'}, name='login'),
        url(r'^logout$', django.contrib.auth.views.logout, {'next_page': '/'}, name='logout'),
        #url('^', include('django.contrib.auth.urls')),
        ]
