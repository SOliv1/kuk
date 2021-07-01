from django.urls import path
from . import views


urlpatterns = [

    path('services/about', views.about, name='about'),
    path('services/our_brands', views.our_brands, name='our_brands'),
    path('services/our_services', views.our_services, name='our_services'),
    path('services/brands', views.brands, name='brands'),
    path('services/contact', views.contact, name='contact'),
    path('services/graphic_design',
         views.graphic_design, name='graphic_design'),
    path('services/digital_marketing',
         views.digital_marketing, name='digital_marketing'),

]