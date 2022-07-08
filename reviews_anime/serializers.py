from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        anime = Anime
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        reviews = Reviews
        fields = '__all__'


class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        raiting = Raiting
        fields = '__all__'


class RaitingStarSerializer(serializers.ModelSerializer):
    class Meta:
        raitingStar = RaitingStar
        fields = '__all__'
