import re
from django.shortcuts import render
from rest_framework import response
from users.models import CustomUser
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
import base64
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import IntegrityError
import random
from django.core.mail import send_mail
from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print(attrs['password'])
        try:
            logger=CustomUser.objects.get(email=attrs['email'])
            
            
            if not logger.has_usable_password():
                print("True aaya")
                logger.set_password("1234@1234")
                logger.save()
                attrs["password"]="1234@1234"
                data = super().validate(attrs)
                refresh = self.get_token(self.user)
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)
                logger.set_unusable_password()
                logger.save()
        
            else:
                print("False aaya")
                data = super().validate(attrs)
                refresh = self.get_token(self.user)
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)
            
            return data
        except CustomUser.DoesNotExist:
            return {
                    "success":False,
                    "msg":"User Doesn't Exist"
            }
        except:
            return {
                "success":False,
                "msg":"Something Went Wrong"
            }

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class TestView(APIView):

    permissions_classes = (AllowAny,)

    def get(self, request):
        works = "this is working"
        return Response({'works': works})

        
def home(request):
   return render(request,'home.html')

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "homee.html"

def facebookLogin(request):
    print("entered login")
    return render(request,'login.html')

"""
{
    "first_name":"Ahsan",
    "last_name":"ALi:,"
    "username":"ahasnalio234",
    "email":"ahasnalio234@mail.commm",
    "phone_no":"12414155",
    "date_of_birth":"1999-03-21",
    "password":"1234@1234"

}
"""

class RegisterView(APIView):
    def post(self,request):
        data=request.data
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        #name=data.get('name')
        username=data.get("username")
        email=data.get("email")
        phone_no=data.get("phone_no")
        date_of_birth=data.get("date_of_birth")
        password=data.get("password")

        print(password)

        try:
            user=CustomUser.objects.create(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                username=username,
                phone_no=phone_no,
                date_of_birth=date_of_birth
            )
            user.set_password(password)
            user.save()
            out=model_to_dict(user)
            return Response(
                {
                    "msg":"User Created","user":out,"pass":user.password                  
                }
            )
        except IntegrityError:
            return Response({"msg":"User Already Exists"})
        except:
            return Response(
                {
                    "msg":"Invalid Data"
                }
            )

class UserView(APIView):
    authentication_classes=[JWTAuthentication,]
    permissions_classes = (IsAuthenticated,)
    def get(self,request):
        user=request.user
        out=model_to_dict(user)
        return Response(

            out
        )
"""
from stockfish import Stockfish
stockfish = Stockfish(path="users/stockfish/stockfish_14.1_win_x64_avx2.exe")

class stockfish_best_move(APIView):
    authentication_classes=[JWTAuthentication,]
    permissions_classes = (IsAuthenticated,)
    def post(self,request):
        data=request.data
        position=data.get("position")
        stockfish.set_position(position)
        best_move=stockfish.get_best_move()
        return Response(best_move)
"""

from .ChessMain import predictMove
class PredictMove(APIView):
    # authentication_classes=[JWTAuthentication,]
    # permissions_classes = (IsAuthenticated,)
    def post(self,request):
        data=request.data
        gameState=data.get("gameState")
        player=data.get("player")
        move=predictMove(gameState,player)
        return Response(

            move
        )


from .engine import stockfish_help
class stockfish_best_move(APIView):
    authentication_classes=[JWTAuthentication,]
    permissions_classes = (IsAuthenticated,)
    def post(self,request):
        data=request.data
        position=data.get("position")
        depth=data.get("depth")
        
        best_move=stockfish_help(position,depth)
        return Response(best_move)

     

"""
class LoginView(APIView):
    def post(self,request):
        data=request.data
        username=data.get("username")
        password=data.get("password")
        try:
            passw=UserDetails.objects.get(username=username).password
            if password==passw:
                return Response(
                    {
                        "msg":"Login Successful"
                    }
                )
        except:
            return Response(
                {
                    "msg":"Invalid Credentials"
                }
            )
"""
