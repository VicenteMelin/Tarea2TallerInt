from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('appburger/', include('appburger.urls')),
    path('admin/', admin.site.urls),
]
