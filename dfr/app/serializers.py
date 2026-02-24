from rest_framework import serializers
from .models import Data
class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email=serializers.EmailField()
    contact=serializers.CharField(max_length=10)
    age=serializers.CharField(max_length=120)
    def create(self, validated_data):
        return Data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
    
