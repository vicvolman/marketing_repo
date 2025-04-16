from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('lead/new/', views.lead_create, name='lead_create'),
    path('lead/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('lead/<int:pk>/update/', views.lead_update, name='lead_update'),
    path('lead/<int:pk>/delete/', views.lead_delete, name='lead_delete'),
    path('contact/', views.public_lead_form, name='public_lead_form'),
    path('contact/thank-you/', views.public_lead_thanks, name='public_lead_thanks'),
    path('test/', views.test_view, name='test'),
    
    
]