from rest_framework import serializers
from rest_framework.fields import ReadOnlyField      #new
from django.contrib.auth import get_user_model

from .models import Item
from users.serializers import UserSerializer


class ItemSerializer(serializers.ModelSerializer):        #new
    user = UserSerializer(read_only=True)

    class Meta:        #new
        model = Item        #new
        fields = ['id', 'name', 'description', 'price', 'user',]        #new

    def create(self, validated_data):
        item = Item.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price = validated_data['price'],
            user = self.context['request'].user
        )
        return item
