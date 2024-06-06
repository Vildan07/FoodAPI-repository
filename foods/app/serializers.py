from rest_framework import serializers
from .models import FoodType, Food, Comment


""" This serializer is used to serialize FoodType objects """


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'

    def create(self, validated_data):
        return FoodType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


""" This serializer is used to serialize Food objects """


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

    def create(self, validated_data):
        return Food.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.food_type = validated_data.get('food_type', instance.food_type)
        instance.price = validated_data.get('price', instance.price)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.save()
        return instance


""" This serializer is used to serialize Comment objects """


class CommentSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.food = validated_data.get('food', instance.food)
        instance.text = validated_data.get('text', instance.text)
        instance.created = validated_data.get('created', instance.created)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

