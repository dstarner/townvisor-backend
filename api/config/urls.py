"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


admin.site.site_header = 'Townvisor'


def _build_includes(path):
    return include(f'{settings.APP_ROOT}.{path}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{settings.API_DOCS_NAME}/', include('rest_framework.urls')),
    path(f'{settings.API_DOCS_NAME}/', include_docs_urls(title='Townvisor API')),
    path('users/', _build_includes('users.urls')),
    path('posts/', _build_includes('posts.urls')),
]

if settings.DEBUG and not settings.USE_S3_STORAGE:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)