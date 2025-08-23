# accounts/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ProfileUpdateSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        serializer = ProfileUpdateSerializer(self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(self.get_object()).data)
