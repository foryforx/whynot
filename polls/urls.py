from django.conf.urls import url,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductdataViewSet)
router.register(r'productfeed', views.ProductfeedViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^$',views.index, name = 'index'),
    url(r'^', include(router.urls)),
]
