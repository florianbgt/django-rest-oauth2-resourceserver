from rest_framework import serializers
from rest_framework.fields import ReadOnlyField      #new
from django.contrib.auth import get_user_model      #new

from .models import Item      #new

User = get_user_model()      #new


class UserSerializer(serializers.ModelSerializer):      #new
    class Meta:      #new
        model = User      #new
        fields = ['id', 'email']      #new


class ItemSerializer(serializers.ModelSerializer):        #new
    user = UserSerializer(read_only=True)      #new

    class Meta:        #new
        model = Item        #new
        fields = ['id', 'name', 'description', 'price', 'user',]        #new

    def create(self, validated_data):      #new
        item = Item.objects.create(      #new
            name=validated_data['name'],      #new
            description=validated_data['description'],      #new
            price = validated_data['price'],      #new
            user = self.context['request'].user      #new
        )      #new
        return item      #new
