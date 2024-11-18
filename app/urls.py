from django.urls import path
from app import views

urlpatterns = [
path('',views.index,name='index'),
path('service/',views.services,name='service'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),
path('blog/',views.blog,name='blog')
]
