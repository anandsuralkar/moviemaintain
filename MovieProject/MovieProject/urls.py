from django.contrib import admin
from django.urls import path,re_path as url
from django.conf.urls import include
from MovieApp import urls,views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),  # Serve index.html for the root URL
    path('', include(urls)),  # Include MovieApp URLs
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)