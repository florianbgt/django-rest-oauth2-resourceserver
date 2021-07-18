from django.urls import path        #new
from .views import ItemList, ItemDetail        #new


urlpatterns = [        #new
    path('', ItemList.as_view()),        #new
    path('<pk>/', ItemDetail.as_view()),        #new
]        #new