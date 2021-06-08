from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
from django.contrib.auth import authenticate, login, logout
from http import HTTPStatus
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAdminUser, IsAuthenticated])
def signup(request):
    try:
        print(request.body)
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password'],
                                        )
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        return HttpResponse(json.dumps({"id":user.id}), status=status.HTTP_200_OK)

    except Exception as e:
        return HttpResponse(json.dumps({"message":str(e)}), status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAdminUser, IsAuthenticated])
def admin_signup(request):
    try:
        print(request.body)
        data = json.loads(request.body)
        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password'],
                                        )
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.is_staff = True
        user.save()
        return HttpResponse(json.dumps({"id":user.id}), status=status.HTTP_200_OK)

    except Exception as e:
        return HttpResponse(json.dumps({"message":str(e)}), status=status.HTTP_400_BAD_REQUEST)