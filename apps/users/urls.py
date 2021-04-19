from django.urls import path, include
from apps.users import views
from rest_framework.routers import DefaultRouter

# Creamos un router y registramos en el las vistas
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('userbooks/', views.UserBooks.as_view()),
]