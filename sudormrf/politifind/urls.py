from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bill/(.*)', views.bill, name='bill'),
    url(r'^politician/(.*)/(bills|votes)*', views.politician, name='politician'),
]
