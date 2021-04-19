from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ,name='home'),
    path('about/',views.about ,name='about'),
    path('store/',views.store,name='store'),
    path('prodview<int:myid>/',views.productview,name='productview'),
    path('search/',views.search,name='search'),
    path('bag/',views.bag,name='bag'),
    path('track/',views.tracker,name='tracker'),
    path('contact/',views.contact,name='contactus'),
]
