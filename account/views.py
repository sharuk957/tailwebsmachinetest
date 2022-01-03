from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# Create your views here.


class RegistrationView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):


    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(password,username)
        if User.objects.filter(username=username).first():
            user = authenticate(username=username,password=password)

            if user is None:
                return Response({'message':'invalid Credential'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message':'Invalid username'},status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
        'access': str(refresh.access_token)
        })

