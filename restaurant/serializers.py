from rest_framework import serializers,permissions
from .models import Menu,Booking
from django.contrib.auth.models import User
class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model=Menu
    fields=['id','title','price','inventory']
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=['url','username','email','groups']
    
class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model=Booking
    fields='__all__'
    
