from django.urls import path
from .views import ItemList, ItemDetail


urlpatterns = [
    path('', ItemList.as_view()),
    path('<pk>/', ItemDetail.as_view()),
]