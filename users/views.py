from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import SignUpSerializer, TokenSerializer

import requests


class SignUpView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer
    def post(self, request):
        response = requests.post(
            'http://localhost:8000/users/signup/',
            data={
                'email': request.data['email'],
                'password': request.data['password'],
                'password2': request.data['password2']
            }
        )
        return Response(response.json())

class GetTokenView(APIView):
    permission_classes = [AllowAny]
    serializer_class = TokenSerializer
    def post(self, request):
        response = requests.post(
            'http://localhost:8000/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['email'],
                'password': request.data['password'],
                'client_id': 'item_API_id',
                'client_secret': 'item_API_secret'
            }
        )
        return Response(response.json())


