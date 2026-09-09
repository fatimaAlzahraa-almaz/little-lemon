from django.shortcuts import render
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu,Booking
from django.contrib.auth.models import User
# Create your views here.

def index(request):
  return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
  queryset=Menu.objects.all()
  serializer_class=MenuSerializer
  
  
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  queryset=Menu.objects.all()
  serializer_class=MenuSerializer
  
class BookingViewSet(viewsets.ModelViewSet):
  queryset=Booking.objects.all()
  serializer_class=BookingSerializer
  permission_classes = [IsAuthenticated]
  
class UserViewSet(viewsets.ModelViewSet):
  queryset=User.objects.all()
  serializer_class=UserSerializer
  permission_classes=[IsAuthenticated]
  
