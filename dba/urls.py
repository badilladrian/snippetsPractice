
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('', include('employee.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
#for restframework login by user 
