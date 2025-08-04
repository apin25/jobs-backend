from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta
from django.db import models
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta

class ExpiringToken(Token):
    class Meta:
        proxy = True

    def expired(self):
        now = timezone.now()
        return self.created < now - timedelta(hours=24)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)

            if not created:
                if token.created < timezone.now() - timedelta(hours=1):
                    token.delete()
                    token = Token.objects.create(user=user)

            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        token_key = request.auth.key if request.auth else None
        if token_key:
            Token.objects.filter(key=token_key).delete()
            return Response({"success": "Logged out"})
        return Response({"error": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
