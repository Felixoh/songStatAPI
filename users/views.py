from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import UserMembership,Membership

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)

        if reg_serializer.is_valid():
            reg_serializer.save()
            newuser = reg_serializer.save()
            get_membership = Membership.objects.get(membership_type='Free')
            UserMembership.objects.create(user=newuser,membership=get_membership)
            return Response({"success":"registration successfull "},status=status.HTTP_201_CREATED)
        else:
            return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status,status.HTTP_400_BAD_REQUEST)  
                 