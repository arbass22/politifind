from django.conf.urls import url

from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bill/(.*)/$', views.bill, name='bill'),
    url(r'^politician/(.*)/(bills|votes)*', views.politician, name='politician'),
    url(r'^politicians/$', views.politicians, name='politicians'),
    url(r'^bills/$', views.bills, name='bills'),
    url(r'^committee/(.*)/(bills|subcomittees)*$', views.committee, name='committee'),
    url(r'^committees/$', views.committees, name='committees'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^vote/(.*)/(yay|nay)*/', views.vote, name='vote')
    url(r'^subscribe/(bill|politician|committee)/(.*)$', views.subscribe, name='subscribe')
]
