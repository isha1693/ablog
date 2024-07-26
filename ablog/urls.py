from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Isha Admin"
admin.site.site_title = "Isha Admin Portal"
admin.site.index_title = "Welcome to Isha's Iconic Blog Portal"

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
