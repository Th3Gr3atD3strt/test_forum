from django.http import HttpResponse
from django.urls import path
from main_site.views import site_view

urlpatterns = [
    path('', site_view, name='main_site'),
]