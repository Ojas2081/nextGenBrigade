from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serilaizers import CompanyRegisterSerializer,CompanyLoginSerializer
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()

def email_send(email_from,email_to,subject,html_message = None,text=None):
    if html_message:
        email = EmailMessage(subject, body=html_message, from_email=email_from, to=[email_to])
        email.content_subtype = "html"
        email.send()
        print("Email Sent successfully !!")
    else:
        email = EmailMessage(subject, body=text, from_email=email_from, to=[email_to])
        email.send()
        print("Email Sent successfully !!")

def home(request):
    return render(request,'company_auth_detail/home.html')

def login_html(request):
    return render(request, 'company_auth_detail/login.html')

def register_html(request):
    return render(request,'company_auth_detail/register.html')


class CompanyRegisterAV(APIView):
    

    def get(self,request,*args,**kwargs):
            if self.request.user.is_company_user:
                users = User.objects.all()
                many = True
            else:
                try:
                    users = User.objects.get(email=request.user.email)
                    many = False
                except:
                    return Response({"error":"Not Authorized"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = CompanyRegisterSerializer(users, many=many)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request,*args,**kwargs):
        serializer = CompanyRegisterSerializer(data=request.data)
        if serializer.is_valid():
            reg_user = serializer.save()
            print("reguserrrr",reg_user)
            data = {}
            data['Message'] = 'User Registered Successfully'
            data['company_email'] = request.data['company_email']
            token = Token.objects.get_or_create(user = reg_user)[0].key
            data['token'] = token
            subject = "Welcome Mail to Our New User"
            path = reverse('login_html')  
            login_url = request.build_absolute_uri(path)
            html_message = render_to_string('company_auth_detail/welcome_email.html', {'company_name': f'{reg_user.company_name}', 'login_url':f'{login_url}','year':2025})


            email_send(settings.EMAIL_HOST_USER,reg_user.company_email,subject,html_message)
            print("Email Sent successfully !!")

            return Response({"Response":data},status=status.HTTP_201_CREATED)
        data = serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
class CompanyLoginAV(APIView):

    def post(self,request,*args,**kwargs):
        serializer = CompanyLoginSerializer(data=self.request.data)
        data = {}
        if serializer.is_valid():
            # print(serializer)
            login_user = User.objects.filter(company_email=self.request.data['company_email']).first()
            print("Login User",login_user)
            
            token = Token.objects.get_or_create(user=login_user)[0].key
            data['token'] = token
            return Response(data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)