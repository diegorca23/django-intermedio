from django.urls import path

from app_coder import views

app_name = 'app_coder'


urlpatterns = [
    path('', views.primer_template),
    path('segundo-template/', views.segundo_template),
    path('tercer-template/', views.tercer_template),
]