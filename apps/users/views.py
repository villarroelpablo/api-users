from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, BookSerializer
from .models import Book
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user = Token.objects.get(key=self.request.auth).user
        serializer.save(user=self.request.user)



class UserBooks(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        token = self.request.auth
        user = Token.objects.get(key=self.request.auth).user
        return Book.objects.filter(user=user)