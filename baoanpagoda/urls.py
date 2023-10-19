"""
URL configuration for baoanpagoda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('', views.index, name="index"),
    path('main_app/', include('main_app.urls')),
    path(_('admin/'), admin.site.urls),
    path('gallery/', include('gallery.urls')),
    path('action/', include('action.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('donation/', include('donation.urls')),
]

urlpatterns += i18n_patterns(path('', views.index, name="index"))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.PLACE_TO_RUN == 'AMAZON':
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)