from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('user_auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('portal/', include('dashboard.urls')),
]
