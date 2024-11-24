from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),
]