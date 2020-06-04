from django.urls import path
from . import views

urlpatterns = [
    path('CV', views.CV, name='CV'),
    path('section/<int:pk>/', views.section_detail, name='section_detail'),
    path('section/<int:pk>/edit/', views.section_edit, name='section_edit'),
]