from datetime import time
from  django.db  import  models 
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rest_framework.views import APIView
from .managers import CustomUserManager
from django.contrib.postgres.fields import ArrayField


# 



class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    
   
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    #name = models.CharField(blank = True, max_length = 200)
    username=models.CharField(max_length=20,unique=True)
    email = models.EmailField(_('email address'), unique = True)
    phone_no=models.CharField(max_length=12,blank=True)
    date_of_birth=models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    #password=models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

#class RegisterView(APIView):
#    def post(self,request):
