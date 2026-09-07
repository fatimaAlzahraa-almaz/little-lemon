from django.urls import path
from . import views

urlpatterns=[
  path('items/',views.MenuItemView.as_view()),
  path('items/<int:pk>/',views.SingleMenuItemView.as_view())
]