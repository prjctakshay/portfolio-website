from django.urls import path
from core.views import index,contactMe

urlpatterns = [
    path('', index, name='index'),
    path('contact_me',contactMe,name='contact_me'),
]
