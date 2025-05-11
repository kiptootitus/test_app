from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class AuthView(APIView):
    def post(self, request):
        action = request.data.get("action")
        username = request.data.get("username")
        password = request.data.get("password")

        if action == "signup":
            if User.objects.filter(username=username).exists():
                return Response({"error": "User exists"}, status=400)
            user = User.objects.create_user(username=username, password=password)
        elif action == "login":
            user = authenticate(username=username, password=password)
            if not user:
                return Response({"error": "Invalid creds"}, status=400)
        else:
            return Response({"error": "Invalid action"}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=200)
