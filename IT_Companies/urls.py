
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("registration.urls")),
    path('software_companies/', include("core.urls")),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    