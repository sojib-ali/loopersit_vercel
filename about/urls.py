from django.urls import path
from . import views


urlpatterns = [
        path('', views.about_us, name='about_us'),
        path('portfolio/', views.portfolio, name='portfolio'),
        path('contact-loopers-it/', views.ContactView.as_view(), name='contact_us'),
        path('contact-success/', views.contact_success, name='contact_success'),
]