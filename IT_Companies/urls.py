
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("registration.urls")),
    path('software_companies/', include("core.urls")),
    
]
