from rest_framework import serializers
from datetime import date

from base.models import car
class carSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    price=serializers.IntegerField()
    date_of_purchase=serializers.DateField()

    def create(self, validated_data):
        return car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name=validated_data.get('name', instance.name)
        print(instance.name)
        instance.price=validated_data.get('price', instance.price)
        instance.date_of_purchase=validated_data.get('date_of_purchase', instance.date_of_purchase)
        instance.save()
        return instance