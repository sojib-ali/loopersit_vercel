from django.urls import path
from . import views


urlpatterns = [
    path('', views.job_list, name='career_list'),
    path('job/<slug:slug>/', views.job_detail, name='career_detail'),
    path('apply/', views.apply_for_job, name='apply_for_job'),
    path('success/', views.application_success, name='application_success'),
]