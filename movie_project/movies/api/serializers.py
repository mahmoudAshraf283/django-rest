from rest_framework import serializers
from movies.models import Movie, Series, Category, Cast

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    casts = CastSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'