from django.conf.urls import url

from . import views
app_name = 'productentity'
urlpatterns = [
    # ex: /productentity/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /productentity/5/
    url(r'^(?P<pk>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /productentity/5/getsku/
    url(r'^(?P<pk>[-\w]+)/getsku/$', views.GetskuView.as_view(), name='getsku'),
    # ex: /productentity/5/wishlist/
    url(r'^(?P<identifier>[-\w]+)/wishlist/$', views.wishlist, name='wishlist'),
]