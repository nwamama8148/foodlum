from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_page', views.about_page , name='about_page'),
    path('services_page', views.services_page , name='services_page'),
    path('users_registration_page',views.signup , name='signup'),
]
