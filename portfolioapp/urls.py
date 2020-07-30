from django.urls import path,include
from . import views

app_name='portfolio_urls'
urlpatterns = [
    path('', views.home,name='home'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('contact/', views.contact,name='contact'),
    path('projects/', views.projects,name='project'),
   
]