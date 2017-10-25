from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^politician/(.*)', views.politician, name='politician'),
    url(r'^bill/(.*)', views.bill, name='bill'),
]
