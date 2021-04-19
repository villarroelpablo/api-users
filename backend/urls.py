from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
]
