from django.urls import path        #new
from .views import SignUpView, GetTokenView, RefreshTokenView ,PasswordChangeView        #new


urlpatterns = [        #new
    path('signup/', SignUpView.as_view()),        #new
    path('token/', GetTokenView.as_view()),        #new
    path('token/refresh/', RefreshTokenView.as_view()),        #new
    path('password/', PasswordChangeView.as_view())        #new
]        #new