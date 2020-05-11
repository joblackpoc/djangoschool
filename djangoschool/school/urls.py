from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage, name='home-page'),
    path('about/', AboutPage, name='about-page'),
    path('contact/', ContactUs, name='contact-page'),
    path('showscore/', ShowScore, name='show-score'),
    path('register/', Register, name='register')
    
]