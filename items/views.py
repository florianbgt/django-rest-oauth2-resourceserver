from rest_framework import generics     #new

from .models import Item     #new
from .serializers import ItemSerializer     #new


class ItemList(generics.ListCreateAPIView):     #new
    queryset = Item.objects.all()     #new
    serializer_class = ItemSerializer     #new


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):     #new
    queryset = Item.objects.all()     #new
    serializer_class = ItemSerializer     #new

