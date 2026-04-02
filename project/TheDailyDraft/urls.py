from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MyHome, name='home'),
    path('pricing', views.Pricing, name='pricing'),
    path('auth/', include('UserAuth.urls')),
    path('blogs/', include('BlogDrafts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 