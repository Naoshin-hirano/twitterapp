from django.urls import path
from twitterapp.api import views

urlpatterns = [
    path('tweets/', views.ListView.as_view(), name="list"),
    path('tweets/<int:pk>/', views.DetailView.as_view(), name="detail"),
]