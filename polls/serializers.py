from django.contrib.auth.models import User, Group
from rest_framework import serializers
from productentity.models import Productdata,Productfeed

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productdata
        fields = ('skuid','title','description','google_product_category','product_type','link','image_link','condition','availability','price','sale_price','brand','gtin')
        
class ProductFeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productfeed
        fields = ('product_feed_url','client')
