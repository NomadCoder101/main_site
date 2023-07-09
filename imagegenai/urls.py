
from django.urls import path
from . import views

urlpatterns = [
    
    path('imagegenai/', views.generate_image_from_text, name='image'),
 
]