from rest_framework.views import APIView        #new
from rest_framework.response import Response        #new
from rest_framework.permissions import AllowAny        #new

from .serializers import SignUpSerializer, TokenSerializer, RefreshTokenSerializer, PasswordChangeSerializer        #new

import requests        #new


class SignUpView(APIView):        #new
    permission_classes = [AllowAny]        #new
    serializer_class = SignUpSerializer        #new
    def post(self, request):        #new
        response = requests.post(        #new
            'http://localhost:8000/users/signup/',        #new
            data={        #new
                'email': request.data['email'],        #new
                'password': request.data['password'],        #new
                'password2': request.data['password2']        #new
            }        #new
        )        #new
        return Response(response.json())        #new

class GetTokenView(APIView):        #new
    permission_classes = [AllowAny]        #new
    serializer_class = TokenSerializer        #new
    def post(self, request):        #new
        response = requests.post(        #new
            'http://localhost:8000/o/token/',        #new
            data={        #new
                'grant_type': 'password',        #new
                'username': request.data['email'],        #new
                'password': request.data['password'],        #new
                'client_id': 'rs-id',        #new
                'client_secret': 'rs-secret'        #new
            }        #new
        )        #new
        return Response(response.json())        #new


class RefreshTokenView(APIView):        #new
    permission_classes = [AllowAny]        #new
    serializer_class = RefreshTokenSerializer        #new
    def post(self, request):        #new
        response = requests.post(        #new
            'http://localhost:8000/o/token/',        #new
            data={        #new
                'grant_type': 'refresh_token',        #new
                'refresh_token': request.data['refresh'],        #new
                'client_id': 'rs-id',        #new
                'client_secret': 'rs-secret'        #new
            }        #new
        )        #new
        return Response(response.json())        #new


class PasswordChangeView(APIView):        #new
    serializer_class = PasswordChangeSerializer        #new
    def put(self, request):        #new
        response = requests.put(        #new
            'http://localhost:8000/users/password/',        #new
            headers={        #new
                'Authorization': request.META.get('HTTP_AUTHORIZATION')        #new
            },        #new
            data={        #new
                'old_password': request.data['old_password'],        #new
                'password': request.data['password'],        #new
                'password2': request.data['password2']        #new
            }        #new
        )        #new
        return Response(response.json())        #new