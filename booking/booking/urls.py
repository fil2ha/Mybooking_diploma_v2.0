from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from booking import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_booking.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    uplpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
