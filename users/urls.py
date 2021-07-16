from django.urls import path
from .views import SignUpView, GetTokenView


urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('token/', GetTokenView.as_view())
]