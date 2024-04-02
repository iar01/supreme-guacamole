from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static, serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apps.rooms.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Booking website"
admin.site.site_header = "Booking  Admin Panel"
admin.site.site_title = "Booking App"
