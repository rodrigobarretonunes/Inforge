# core/urls.py

from django.contrib import admin
from django.urls import path, include
from summarizer import views as views_summarizer
from dashboard import views as views_dashboard
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth
    path('summarizer/', views_summarizer.summarizer, name='summarizer'),
    path('dashboard/',views_dashboard.dashboard,name = 'dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)