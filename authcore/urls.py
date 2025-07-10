# authcore/urls.py

from django.urls import path
from .views import manage_users_view

urlpatterns = [
    path('manage_profiles/', manage_users_view, name='manage_profiles'),
]
